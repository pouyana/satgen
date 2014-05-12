#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Satellite Simulation Configuration Parser.
Reads data from the Text or XML config file
"""

import ConfigParser
import io
from logger import Logger
from config_converter import Converter
from ConfigParser import ParsingError

class Config:

    config = ConfigParser.ConfigParser()

    def check_file(self, address):
        """
        check if the file has the right syntax.
        """
        f = open(address,"r+")
        try:
            self.config.read(address)
        except ParsingError as e:
            print e

    def read_file(self,address):
        self.config.read(address)
        print self.config.get("Space Object","Mass")

config = Config()
config.check_file("sample_1_sim.txt")
