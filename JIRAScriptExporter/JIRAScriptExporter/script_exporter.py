'''
Created on 25/mar/2016

@author: Andrea Dell'Orto
'''

import configparser
import inspect
import os

from JIRAScriptExporter.JIRA_reader import JIRAReader
from JIRAScriptExporter.instruction_creator import InstructionCreator


def ConfigFileReader():
    cfgFilePath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '\JIRAExporter.cfg'
    config = configparser.ConfigParser()
    config.readfp(open(cfgFilePath))
    return config

if __name__ == '__main__':
    reader = JIRAReader()
    file = reader.get_file(input("Issue number: "))
    inst_creator = InstructionCreator(file)
    inst_creator.generate_instructions()