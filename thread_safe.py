import os
import threading

class child(threading.Thread):
    def __init__(self, initpath ):
        # initpath could be a string fed to many initializations 
        os.chdir( initpath )

    def run(self ):
        print os.getcwd()
        child().start() # prints "/username/path"
        custom_path_child = child(
                initpath = '/home/poa32kc/Program',
                ).start() # prints "/home/username/somefolder/"


os.chdir('/') # The process is changing directory

#child("/").start() # prints "/"
#child("/").start() # prints "/"
