#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Manages MASTER Program runs on the System.
Reads from Database, create the master.cfg and other MASTER
Componnets.
To use the code you need MASTER-2009 installed, please Download it 
from: https://sdup.esoc.esa.int
"""

import subproccess
import os
import sys
from database import DB

class Master:

    def __init__(self, master_path, db):
        self.set_master_path(master_path)
        self.set_db(db)

    def get_master_path(self):
        """
        Returns the master absolute path set
        """
        return self.master_path

    def set_master_path(self, master_path):
        """
        Sets the Master Absolute Path
        """
        self.master_path= master_path

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


