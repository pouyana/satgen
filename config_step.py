#!/bin/env python
# -*- coding: utf-8 -*-
"""
This class is menat to read step configurations
for the different parameters related to the satelite.
the syntax of the step parameters should be like this

[Parameter Name]
Start Value  = float / int
Step = float / int
End Value = float / int
...
...
...

This configuration will be read and put to a matrix
so diffrenet satellite will be creared.
"""
from logger import Logger
import ConfigParser
import itertool


class ConfigStep:
    def __init__(self, log_level="ERROR"):
        self.logger = Logger(log_level)
        self.log = self.logger.get_logger()
        self.step_conf = dict()

    def set_step_conf(self, conf):
        """
        Set the step config
        """
        return self.step_conf

    def get_step_conf(self):
        """
        Returns the step conf
        """
        return self.step_conf

    def get_conf_parser(self):
        """
        Generates a ConfigParser instance
        """
        return ConfigParser.ConfigParser()

    def read_conf(self, address):
        """
        Reads the config file contents and
        generates a configuration dict
        """
        config = self.get_conf_parser()
        config.read(address)
        sections = config.sections()
        for section in sections:
            self.get_step_conf()[section] = dict()
            for option in config.options(section):
                config_value=config.get(section, option, True)
                self.get_step_conf()[section][option.title()] = config_value

    def do_steps(self):
        """
        Returns all the possible values for different paramters in array
        With the help of this results, the combination matirx will be created
        """
        steps = self.get_step_conf()
        all_step_config = dict()
        for k,v in steps.items():
            tmp_list = list()
            all_step_config[k] = tmp_list
            start = v["Start Value"]
            end = v["End Value"]
            tmp_list.append(float(start))
            while float(start) < float(end):
                start = float(start) + float(v["Step"])
                tmp_list.append(start)
        return all_step_config

    def get_combinations(self):
        """
        Returns all the possible combinations from the given dict
        """


steps = ConfigStep()
steps.read_conf("steps.cfg")
print steps.do_permutation()
