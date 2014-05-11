#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Satellite Simulation Configuration Parser.
Reads data from the Text or XML config file
"""

import ConfigParser
import io



class Config:
    config = ConfigParser.ConfigParser()
    def read_file(self,address):
        self.config.read(address)
        print self.config.get()

config = Config()
config.read_file("sample_1_sim.txt")
