#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import tempfile
import platform
import datetime
import shutil
import re
import threading
import subprocess
import shlex
from time import sleep
from config_dict import ConfigDict
from database import DB


class Extrapolate():
    """
    Extrapolate generated satellites.
    With the help of database search
    """
    def set_db(self,db):
        """
        Sets the Database
        """
        self.db = db

    def get_db(self):
        """
        Returns the database
        """
        return self.db

    def set_root(self, root):
        """
        Sets the root folder for the simulation files
        """
        self.root = root

    def get_root(self):
        """
        Retruns root
        """
        return self.root

    def getFinalStateValue(self, key, file_name):
        """
        Get the final status value that can be set in the database
        """
        from xml.dom.minidom import parse
        doc = parse(file_name)
        node = doc.getElementsByTagName("finalState")[0].getElementsByTagName(key)
        try:
            tmp = float(node[0].firstChild.nodeValue)
        except:
            self.end(50, "Key <" + key + "> not found in final bulletin")
        return tmp

    def getFinalDate(self,file_name):
        """
        Get the end date
        """
        from xml.dom.minidom import parse
        doc = parse(file_name)
        node = doc.getElementsByTagName("finalState")[0].getElementsByTagName("date")
        return node[0].firstChild.nodeValue

    def getFinalType(self,file_name):
        """
        Get the Simulation type in final mode.
        most of the time shoud be the same as initType
        """
        import xml.etree.ElementTree as ET
        tree = ET.parse(file_name)
        root = tree.getroot()
        finalstate = root.findall(".//finalState/bulletin")
        self.final_type = list(finalstate[0])[1].tag
        print list(finalstate[0])[1].tag
        return list(finalstate[0])[1].tag

    def get_file_list(self):
        """
        returns the files listed in root folder
        """
        return os.listdir(self.get_root())
    
    def get_name(self,file_name):
        """
        returns the sat name in database from the filename
        """
        f = file_name.split("_a_sim.xml")[0]
        return f

    def convert_to_tuple(self, space_object_id, file_name):
        """
        converts the finalState to tuple to be added to the database
        """
        import xml.etree.ElementTree as ET
        tree = ET.parse(file_name)
        self.final_type = self.getFinalType(os.path.abspath(file_name))
        root = tree.getroot()
        finalstate = root.findall(".//finalState/bulletin/"+self.final_type)
        key_tuple = tuple()
        value_tuple = tuple()
        qu_tuple = tuple()
        qu = "?,"
        qu_tuple = "(?,?, "
        for f in finalstate[0].iter():
            if(f.tag!=self.final_type):
                key_tuple = key_tuple+(f.tag, )
                value_tuple = value_tuple + (f.text,)
                qu_tuple = qu_tuple+qu
        key_tuple = key_tuple + ("spaceObjectId", "date")
        value_tuple = value_tuple + (space_object_id[0], self.getFinalDate(os.path.abspath(file_name)))
        qu_tuple = qu_tuple[:-1]+")"
        return {"key":key_tuple, "value":value_tuple, "qu": qu_tuple}

#    def extrapolate(self,f):
#        if(os.path.splitext(f)[1]==".xml" and not re.search("out",f)):
#            object_id=db.get_sat_id_by_name(self.get_name(f))
#            os.chdir(self.get_root())
#            option=" -i " + os.path.abspath(f) + " -o " + os.path.abspath(f)+"_out"         
#            os.chdir("/home/poa32kc/Programs/Stela/bin")                    
#            command_line = "./stela-batch.sh"+option
#            args = shlex.split(command_line)
#            CR = subprocess.call(args)
#            os.chdir(self.get_root())
#            config_tuple = self.convert_to_tuple(object_id, os.path.abspath(f)+"_out_sim.xml")
#            self.db.insert_final_state(config_tuple)


class ExtrapolateThread(threading.Thread):
    """
    The Extrapolate Multithread mechanisem
    """
    def __init__(self,f,ex):
        threading.Thread.__init__(self)
        self.ex = ex
        self.f = f
        option=" -i " + ex.get_root()+f + " -o " + ex.get_root()+f+"_out"+" -eph_stela "+ ex.get_root()+f+"_out_eph " +"mean "+"keplerian"
        self.command_line = "./stela-batch.sh"+option
        print self.command_line

    def run(self):
        if(os.path.splitext(self.f)[1]==".xml" and not re.search("out",self.f)):
            db=DB("/home/poa32kc/Programs/satgen/satgen.db")
            object_id=db.get_sat_id_by_name(self.ex.get_name(self.f))
            args = shlex.split(self.command_line)
            CR = subprocess.call(args)
            from time import sleep
            sleep(1)
            config_tuple = self.ex.convert_to_tuple(object_id, ex.get_root()+self.f+"_out_sim.xml")    
            db.insert_final_state(config_tuple)

ex=Extrapolate()
ex.set_root("/home/poa32kc/Programs/satgen/sim/")
os.chdir("/home/poa32kc/Programs/Stela/bin")
thread_list=[]
for f in ex.get_file_list():
    #6 multithread
    while(len(thread_list)>6):
        while(len(thread_list)!=0):
            t = thread_list.pop()
            t.join()
    thread0=ExtrapolateThread(f,ex)
    thread0.start()
    thread_list.append(thread0)

