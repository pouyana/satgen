#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os
import tempfile
import platform
import datetime
import shutil
from time import sleep
import re
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
        return list(finalstate[0])[1].tag

    def update_final_state(self, final_id, file_name):
        """
        Update final state values in database
        """
        import xml.etree.ElementTree as ET
        tree = ET.parse(file_name)
        root = tree.getroot()
        finalstate = root.findall(".//finalState/bulletin/"+self.final_type)
        for fls in finalstate[0].iter():
            if (fls.tag!=self.final_type):
                self.get_db().update_value("finalState", fls.tag, final_id, fls.text)

    
    def get_file_list(self):
        """
        returns the files listed in root folder
        """
        return os.listdir(self.get_root())
    
    def get_name(self,file_name):
        """
        returns the sat name in database from the filename
        """
        f=file_name.split("_a_sim.xml")[0]
        return f
    
    def extrapolate(self):
        import subprocess, shlex
        db=DB("satgen.db")
        self.set_db(db)
        for f in self.get_file_list():
            if(os.path.splitext(f)[1]==".xml" and not re.search("out",f)):
                object_id=db.get_sat_id_by_name(self.get_name(f))
                os.chdir(self.get_root())
                option=" -i " + os.path.abspath(f) + " -o " + os.path.abspath(f)+"_out"         
                os.chdir("/home/poa32kc/Programs/Stela/bin")                    
                command_line = "./stela-batch.sh"+option
                args = shlex.split(command_line)
                CR = subprocess.call(args)
                os.chdir(self.get_root())
                final_type = self.getFinalType(os.path.abspath(f)+"_out_sim.xml")
                final_id = self.get_db().insert_final_state(final_type,object_id[0])
                self.update_final_state(final_id,os.path.abspath(f)+"_out_sim.xml")
                self.db.update_value("finalState", "date", final_id, self.getFinalDate(os.path.abspath(f)+"_out_sim.xml"))

ex=Extrapolate()
ex.set_root("/home/poa32kc/Programs/Python/satgen/sim/")
ex.extrapolate()
