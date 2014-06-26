#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Manages MASTER Program runs on the System.
Reads from Database, create the master.cfg and input files.
To use the code you need MASTER-2009 installed, please Download it 
from: https://sdup.esoc.esa.int
To convert deg<->rad pint framework is used.
"""

import subprocess
import threading
from datetime import datetime, date, time
import os
import re
import sys
import shutil
from database import DB
from unit_converter import UnitConverter


class Master:

    def __init__(self, master_path, db, default_dir_path):
        self.set_master_path(master_path)
        self.set_default_dir(default_dir_path)
        self.set_db(db)

    def set_default_dir(self, default_path):
        """
        set the defualt abs path
        """
        self.default_dir = default_path

    def get_default_dir(self):
        """
        get the default abs path
        """
        return self.default_dir

    def get_master_path(self):
        """
        Returns the master absolute path set
        """
        return self.master_path
    
    def set_name_vars(self):
        """
        Sets the name variable tuple
        """
        self.name_vars = self.get_space_objects()["names"]

    def get_name_vars(self):
        """
        Returns the name variable tuple, set from db
        """
        return self.name_vars

    def set_master_path(self, master_path):
        """
        Sets the Master Absolute Path
        """
        self.master_path = master_path

    def get_db(self):
        """
        Return database instance
        """
        return self.db

    def set_db(self,db):
        """
        Sets the database instance
        """
        self.db = db

    def create_files(self,db_tuple):
        """
        creates the needed files for the MASTER2009
        """
        #master.cfg
        master_cfg_content = {"default_dir":os.getcwd(), "master_dir":self.get_master_path()}
        fh = open(self.get_default_dir()+"/../sample_files/master.cfg","r")
        data = fh.read()
        #** see http://stackoverflow.com/questions/36901
        data = data.format(**master_cfg_content)
        ff = open(os.getcwd()+"/master.cfg","w")
        ff.write(data)
        fh.close()
        ff.close()
        #master.inp
        master_inp_cont = self.master_inp_cont_gen(db_tuple)
        fh = open(self.get_default_dir()+"/../sample_files/master.inp","r")
        data = fh.read()
        data = data.format(**master_inp_cont)
        print data
        ff = open(os.getcwd()+"/input/master.inp","w")
        ff.write(data)
        fh.close()
        ff.close()
        #defaults
        shutil.copyfile(self.get_default_dir()+"/../sample_files/default.def",os.getcwd()+"/input/default.def")
        shutil.copyfile(self.get_default_dir()+"/../sample_files/default.sdf",os.getcwd()+"/input/default.sdf")
        shutil.copyfile(self.get_default_dir()+"/../sample_files/default.con",os.getcwd()+"/input/default.con")


    def master_inp_cont_gen(self,db_tuple):
        """
        Creates the master inp content dict
        """
        un_cnv=UnitConverter()
        result = {}
        for t in self.get_name_vars():
            if t not in ["init_date", "final_date" , "init_semiMajorAxis", "name", "id", "final_id", "final_semiMajorAxis", "final_eccentricity" , "init_eccentricity"]:
                result[t]=un_cnv.rad_to_deg(db_tuple[self.get_i(t)])
            if t in ["init_semiMajorAxis", "final_semiMajorAxis"]:
                result[t]=un_cnv.m_to_km(db_tuple[self.get_i(t)])
            if t in ["init_date", "final_date"]:
                result[t]=self.format_date(db_tuple[self.get_i(t)])
            if t in ["name", "final_eccentricity", "init_eccentricity"]:
                result[t]=db_tuple[self.get_i(t)]
        return result

    def get_i(self,variable):
        """
        Retruns the index of name variable
        """
        return self.search_in_tuple(self.get_name_vars(),variable)

    def format_date(self,date):
        """
        Formats the date from STELA mode to MASTER2009
        YYYYMMDDT.HHH->yyyy mm dd hh
        """
        d = datetime.now()
        d = d.strftime("%Y %m %d %H")
        if(re.search("T",date)):
            d = " ".join([date.split("T")[0].replace("-"," "),date.split("T")[1].split(":")[0]])
        return d

    def get_space_objects(self):
        """
        creates the folders and set the env
        variable so the master simulation
        can be run
        """
        return self.db.get_space_objects_data()

    def search_in_tuple(self,t,s):
        """
        Search in the tuple, get the index back
        """
        counter = 0
        for i in t:
            if i == s:
                return counter
            counter=counter+1

    def run_master(self,db_tuple):
        """
        Runs master
        """
        work_dir = self.get_default_dir()+"/"+db_tuple[self.search_in_tuple(self.get_name_vars(),"name")]
        os.mkdir(work_dir)
        os.chdir(work_dir)
        os.mkdir("output")
        os.mkdir("input")
        self.create_files(db_tuple)
        subprocess.Popen(self.get_master_path()+"/"+"master_linux_64")
        os.chdir(self.get_default_dir())

class MasterThread(threading.Thread):
    def __init__(self,divider):
        self.divider = divider

db=DB("satgen.db")
ma=Master("/home/poa32kc/ESA",db,"/home/poa32kc/Programs/satgen/master_sim")
space_objects = ma.get_space_objects()
space_tuple_sample = space_objects["data"][1]
ma.set_name_vars()
ma.run_master(space_tuple_sample)
