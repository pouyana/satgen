#!/usr/bin/env python

"""A basic fork in action"""

import os

def my_fork():
    child_pid1 = os.fork()
    child_pid2 = os.fork()
    child_pid3 = os.fork()
    if child_pid2 == 0:
        print "Child Process: PID# %s" % os.getpid()
    else:
        print "Parent Process: PID# %s" % os.getpid()

if __name__ == "__main__":
    my_fork()
