'''
Created on 25/mar/2016

@author: Andrea Dell'Orto
'''

import configparser
import inspect
import os
import JIRAScriptExporter.JIRA_reader

def ConfigFileReader():
    cfgFilePath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '\JIRAExporter.cfg'
    config = configparser.ConfigParser()
    config.readfp(open(cfgFilePath))
    return config

if __name__ == '__main__':
    jira_reader = JIRAScriptExporter.JIRA_reader()
    file = jira_reader.get_file(input("Issue number: "))
    