'''
Created on 25/mar/2016

@author: Andrea Dell'Orto
'''

from JIRAScriptExporter.JIRA_reader import JIRAReader
from JIRAScriptExporter.instruction_creator import InstructionCreator


if __name__ == '__main__':
    reader = JIRAReader()
    #file = reader.get_file(input("Issue number: "))
    file = reader.get_file('BPMPEF-1906')
    inst_creator = InstructionCreator(file,reader.get_option())
    inst_creator.generate_instructions()