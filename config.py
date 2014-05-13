#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sets/gets different configurations.
If a configuration parameter not given to
the satgen it uses the values in the file.
Satgen can not accept all the parameters
from the command line so please create a configuration file.
"""

from logger import Logger


class Config:
    def __init__(self, log_level="ERROR"):
        logger = Logger(log_level)
        self.log = logger.get_logger()
        self.conf = {}

    def set_abstract_item(self, section, option, value):
        """
        Adds items to the config array
        """
        if section in self.conf.keys():
            self.conf[section][option] = value
        else:
            self.conf[section] = {}
            self.conf[section][option] = value

    def get_abstarct_item(self, section, option):
        """
        Gives the item value back.
        """
        try:
            self.conf[section][item]
        except KeyError as e:
            self.log.error("Key or value not found please try again")

    def get_conf(self):
        """
        Gives the conf dict back
        """
        return self.conf

    def set_model(self, model):
        """
        Set Model in General
        """
        self.set_abstract_item("General", "Model", model)

    def get_model(self):
        """
        Gives Model back
        """
        return self.get_abstarct_item("General", "Model")

    def set_mass(self, mass):
        """
        Set the mass of the space object
        """
        self.set_abstract_item("Space Object", "Mass", mass)

    def get_mass(self):
        """
        Gives the Mass of the Object back.
        """
        return self.get_abstarct_item("Space Object", "Mass")

    def get_author(self):
        """
        Gives the Author back
        """
        return self.get_abstarct_item("General", "Author")

conf = Config()
conf.set_model("GTO")
conf.set_mass(2)
print conf.get_conf()
