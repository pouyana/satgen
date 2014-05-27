#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
SatGen is a satellite generator for the STELA (and soon MASTER-2009)
simulation environments. It can be used for batch simulations.
The batch mode it self will also be included in future.
"""

import argparse
import random
import string
from config import Config
from config_converter import Converter
from config_parser import ConfParser
from config_step import ConfigStep


def set_verbose_level(level, quiet=False):
    """
    Setting verbosity level.
    """
    verbose = "ERROR"
    if(level == 0 or quiet):
        verbose = "ERROR"
    elif(level == 1):
        verbose = "WARNING"
    elif (level == 2):
        verbose = "INFO"
    elif (level > 2):
        verbose = "DEBUG"
    return verbose


def name_generator(size=8, chars=string.ascii_uppercase + string.digits):
    """
    Generates Random UPPERCASE names for the satellite taken from
    http://stackoverflow.com/q/2257441
    """
    return ''.join(random.choice(chars) for _ in range(size))


def set_name(name=False):
    """
    Set the name of the satellite
    """
    if not name:
        name = name_generator()
    return name

def set_options(conf, combination, options):
    """
    Set the options with the different combinations
    """

def main():
    """
    Main Function, contains everything else.
    """
    parser = argparse.ArgumentParser(
        description="SatGen, the Satellite generator.")
    group_mutal = parser.add_mutually_exclusive_group()
    group_mutal.add_argument(
        "-v",
        "--verbose",
        help="verbose logging",
        action="count",
        default=0)
    group_mutal.add_argument(
        "-q",
        "--quiet",
        help="quiet mode",
        action="store_true")
    parser.add_argument(
        "-n",
        "--name",
        nargs='?',
        help="satellite name (default random 8 chars)")
    parser.add_argument(
        "-c",
        "--config",
        nargs='?',
        help="config file, read config from cfg")
    parser.add_argument(
        "-s",
        "--step",
        nargs='?',
        help="step file for the generation of xml files")
    parser.add_argument(
        "-o",
        "--outputfolder",
        nargs='?',
        help="output folder")
    args = parser.parse_args()
    verbose = set_verbose_level(args.verbose, args.quiet)
    name = set_name(args.name)
    config = Config(log_level=verbose)
    if(args.step):
        steps = ConfigStep()
        steps.read_file(args.step)
        options = steps.get_options()
        combinations = steps.get_combinations()
    if(args.config):
        conf_parser = ConfParser(log_level=verbose)
        config_from_file = conf_parser.read_file(args.config)
        config.set_conf(config_from_file)
        config.set_space_object_name(name)
        config.set_edge_length(0.1)
    if(combinations and options):
        for combination in combinations:
            

        print config.convert_to_xml()
        print config.get_xml_file_name()
    else:

if (__name__ == "__main__"):
    main()
