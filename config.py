#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Sets/get different configurations.If a configuration parameter not given to the satgen it uses the values in the file.
Satgen can not accept all the parameters from the command line so please create a configuration file.
"""

from logger import Logger


class Config:
    def __init__(self, log_level="ERROR"):
        logger = Logger(log_level)
        self.log = logger.get_logger()
        self.conf = {}
    
    def get_conf(self):
        """
        Gives the conf dict back
        """
        return self.conf

    def set_conf(self,new_conf):
        """
        Sets the new configuration from the old
        """
        old_conf = self.conf

