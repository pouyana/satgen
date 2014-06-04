#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
The Interface to the Batch simulator of Stela
it will connect to the batch simulator with files
and run the evaluation
"""
import sys,os
import tempfile
import platform
import datetime
import shutil
from time import sleep
from config_dict import ConfigDict

class Simulate:
    def __init__(self, stela_root, input_file, sim_out, space_object_id, db):
        self.root = stela_root
        self.input_file = input_file
        self.output_folder = sim_out
        self.db_id = space_object_id
        self.config_dict = ConfigDict()
        self.db = db
        self.temp_file = self.input_file + "stela_tmp_sim.xml"
        self.work_file = tempfile.NamedTemporaryFile().name + "stela_work_sim.xml"
        self.DEBUG_MODE = True
    
    def debug(self, mess):
        if self.DEBUG_MODE:
            print "DEBUG# " + mess

    def getFinalStateValue(self, key):
        """
        Get the final status value that can be set in the database
        """
        from xml.dom.minidom import parse
        doc = parse(self.temp_file)
        node = doc.getElementsByTagName("finalState")[0].getElementsByTagName(key)
        try:
            tmp = float(node[0].firstChild.nodeValue)
        except:
            self.end(50, "Key <" + key + "> not found in final bulletin")
        return tmp

    def getFinalDate(self):
        """
        Get the end date
        """
        from xml.dom.minidom import parse
        doc = parse(self.temp_file)
        node = doc.getElementsByTagName("finalState")[0].getElementsByTagName("date")
        return node[0].firstChild.nodeValue
    
    def getFinalType(self):
        """
        Get the Simulation type in final mode.
        most of the time shoud be the same as initType
        """
        import xml.etree.ElementTree as ET
        tree = ET.parse(self.temp_file)
        root = tree.getroot()
        finalstate = root.findall(".//finalState/bulletin")
        return list(finalstate[0])[1].tag

    def update_final_state(self, final_id):
        """
        Update final state values in database
        """
        import xml.etree.ElementTree as ET
        tree = ET.parse(self.temp_file)
        root = tree.getroot()
        finalstate = root.findall(".//finalState/bulletin/"+self.getFinalType())
        for fls in finalstate[0].iter():
            if (fls.tag!=self.getFinalType()):
                self.db.update_value("finalState", fls.tag, final_id, fls.text)


    def copy(self, src, dest):
        """
        Copy the file with the help of buffer
        """
        self.debug("copy " + src + " to " + dest)
        try:
            s=open(src,"r" )
        except:
            self.end(10, "File <" + src +"> not found")
        try:
            #Open file for writing
            t=open(dest,"w+" )
        except:
            end(20, "File <" + dest +" > not found")
        while 1:    
            # Read 1 buffer of file
            buf=s.read(1)
            if buf:
                t.write(buf)
            else:
                break
        s.close()
        t.close()

    def moveExtrapolationFile(self, src, dest):
        """
        Move extrapolierte File
        """
        self.remove_file(dest)
        os.rename(src,dest)
        self.remove_file( dest.replace(".xml",".txt"))
        os.rename(src.replace(".xml",".txt"), dest.replace(".xml",".txt"))
    
    def end(self, CR, mess):
        """
        Ends the programs
        """
        print "END PROG (CR=" + str(CR) + ") # " + mess
        raw_input('Press enter to finish the program...')
        sys.exit(CR)

    def remove_file(self, filename):
        """
        Remove the given file
        """
        if os.path.isfile(filename):
            os.remove(filename)
        if os.path.isfile(filename):
           end(30, "Error when remove file <" + filename +">")

    def choseprog(self):
        """
        Choose the right platform batch
        """
        platf=platform.system()
        if platf == 'Linux':
            cmd = os.path.join(self.root,"bin","stela-batch.sh")
        elif platf == 'Windows':
            cmd = os.path.join(self.root,"bin","stela-batch.bat")
        else:
            self.end(100, "unknown OS")
        self.debug("PROG : " + cmd)

        return cmd

    def extrapolate(self):
        """
        Extrapolate with Stela
        """
        import subprocess, shlex
        prog=self.choseprog()
        option=" -i " + self.input_file + " -o " + self.temp_file
        os.chdir("/home/poa32kc/Programs/Stela/bin")
        command_line = "./stela-batch.sh"+option
        args = shlex.split(command_line)
        platf=platform.system()
        CR = 1
        if platf == 'Linux':
            while(CR!=0):
                print args
                CR = subprocess.call(args)
                print CR
        elif platf == 'Windows':
            CR = os.system( os.path.basename(prog) + option)
        final_type = self.getFinalType()
        final_id = self.db.insert_final_state(final_type,self.db_id)
        self.update_final_state(final_id)
        self.db.update_value("finalState", "date", final_id, self.getFinalDate())
