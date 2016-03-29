'''
Created on 29/mar/2016

@author: A22J
'''
import configparser
import inspect
import os


class ConfigFileReader(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        cfgFilePath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '\JIRAExporter.cfg'
        config = configparser.ConfigParser()
        config.readfp(open(cfgFilePath))
    