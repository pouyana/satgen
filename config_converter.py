#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converts Text simulation config created by STELA to Shlex configs.
"""

import io
import re
import sys
from logger import Logger
from version import Version


class Converter:
    def __init__(self, log_level="ERROR"):
        """
        Initial Model adds Loging
        """
        logger = Logger(log_level)
        self.log = logger.get_logger()

    def read_file(self, file_address):
        """
        Reads the file, if not found breaks and logs an
        ERROR and breaks the program.
        """
        try:
            f = open(file_address, "r+")
        except IOError as e:
            self.log.error("I/O error({0}): {1}".format(e.errno, e.strerror))
            raise
        return f

    def get_file_container(self, f):
        """
        Get the file as a dict of extension and name
        """
        file_name = f.name
        name_ext = file_name.split(".")
        ext = name_ext[len(name_ext)-1]
        del name_ext[-1]
        name = ".".join(name_ext)
        file_container = {"name": name, "ext": ext}
        return file_container

    def convert_file(self, file_address):
        """
        Get the txt file and convert it to the
        shelx config file
        """
        version = Version()
        version_tag = version.get_version()
        f = self.read_file(file_address)
        written_file = open(self.get_file_container(f)["name"]+".cfg", 'w')
        written_file.write(
            "#Config file generated by SatGen V. "+version_tag)
        for line in list(f):
            line = re.sub(":", "=", line)
            line = re.sub("\[ ", "[", line)
            line = re.sub(" \]", "]", line)
            line = line.strip()
            line = line+"\n"
            try:
                written_file.write(line)
                self.log.debug(written_file.name+" is written to the desk")
            except IOError as e:
                self.log.error(
                    "I/O error({0}): {1}".format(e.errno, e.strerror))
                raise
        written_file.close()
        f.close
