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
from config_converter import Converter


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
    args = parser.parse_args()
    verbose = set_verbose_level(args.verbose, args.quiet)
    name = set_name(args.name)
    converter = Converter(log_level=verbose)
    converter.read_file("aaa")
    print name

if (__name__ == "__main__"):
    main()
