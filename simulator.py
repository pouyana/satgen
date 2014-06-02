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
from database import DB
from config_dict import ConfigDict

class Simulate:
    def __init__(self, stela_root, input_file, sim_out, space_object_id):
        self.root = stela_root
        self.input_file = input_file
        self.output_folder = sim_out
        self.db_id = space_object_id
        self.config_dict = ConfigDict()
        self.db = DB("satgen.db")
        self.temp_file = self.output_folder + os.path.basename(input_file) + "_tmp_sim.xml"
        self.work_file = self.output_folder + os.path.basename(input_file) + "_work_sim.xml"
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
        import subprocess
        prog=self.choseprog()
        option=" -i " + self.work_file + " -o " + self.temp_file
        os.chdir(os.path.dirname(os.path.normpath(prog)))
        platf=platform.system()
        if platf == 'Linux':
            CR=os.system("./" + os.path.basename(prog) + option  )
        elif platf == 'Windows':
            CR=os.system( os.path.basename(prog) + option)
        else:
            end(105, "unknown OS")
        if CR != 0:
            self.end(CR, "Error when launching extrapolation")
        if not os.path.isfile(self.temp_file):
            self.end(110, "Error when write output file during launching extrapolation")
        final_type = self.getFinalType()
        final_id = self.db.insert_final_state(final_type,29)
        if not os.path.isfile(self.work_file):
            end(120, "Error when move temporary file in working file")

simulator=Simulate("/home/poa32kc/Programs/Stela", "sim/BNGNIAL0_2.0_0.4_sim.xml","/home/poa32kc/Programs/Python/satgen/sim/", 1)
simulator.copy(simulator.input_file, simulator.work_file)
simulator.extrapolate()
