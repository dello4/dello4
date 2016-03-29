'''
Created on 29/mar/2016

@author: Andrea Dell'Orto
'''
import configparser
import inspect
import os


class ConfigFileReader(object):
    '''
    classdocs
    '''
    options = ""

    def __init__(self):
        cfgFilePath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '\JIRAExporter.cfg'
        config = configparser.ConfigParser()
        config.readfp(open(cfgFilePath))
        self.options = config