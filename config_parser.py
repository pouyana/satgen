#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Satellite Simulation Configuration Parser.
Reads data from the Text or XML config file
"""

import ConfigParser
import io
import os.path
from logger import Logger
from config_converter import Converter


class Config:
    def __init__(self, log_level="ERROR"):
        self.config = ConfigParser.ConfigParser()
        self.logger = Logger(log_level)
        self.log = self.logger.get_logger()

    def check_file(self, address):
        """
        check if the file has the right syntax.
        """
        converter_container = Converter()
        f = open(address, "r+")
        directory = os.path.dirname(os.path.abspath(address))
        file_container = converter_container.get_file_container(f)
        file_name = file_container["name"]
        try:
            self.config.read(f.name)
            return f.name
        except ConfigParser.ParsingError as e:
            self.log.warning(
                "The file was not cfg, converted to cfg file")
            if(file_name+".cfg" in os.listdir(directory)):
                new_name = raw_input("""
                    The file allready exists in this directory,
                    give a new name (don't forget the .cfg)?
                    """)
                written_file_name = new_name.strip()
                converter_container.convert_file(f.name, written_file_name)
                file_name = written_file_name
            else:
                file_name = converter_container.convert_file(f.name)
            return file_name

    def read_file(self, address):
        """
        Reads the config file contents and
        generate a configuration dict
        """
        file_name = self.check_file(address)
        self.config.read(file_name)
        print self.config.get("Space Object", "Mass")

config = Config()
config.read_file("sample_1_sim.txt")
