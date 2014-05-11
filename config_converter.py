#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converts Text simulation config created by STELA to Shlex configs.
"""

import io
import re
import sys
from logger import Logger


class Converter:
    def __init__(self,log_level="ERROR"):
        """
        Initial Model adds Loging
        """
        logger = Logger(log_level)
        self.log = logger.get_logger()


    def read_file(self, file_address):
        """
        Reads the file, if not found breaks and logs an ERROR and breaks the program.
        """
        try:
            f = open(file_address, "r+")
        except IOError as e:
            self.log.error("I/O error({0}): {1}".format(e.errno, e.strerror))
            raise
        return f

#converter = Converter()
#converter.read_files("sample_1_sim.txt")
