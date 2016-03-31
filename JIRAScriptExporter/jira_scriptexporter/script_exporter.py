'''
Created on 25/mar/2016

@author: Andrea Dell'Orto
'''

from jira_scriptexporter.jira_reader import JIRAReader
from jira_scriptexporter.instruction_creator import InstructionCreator

def run():
    reader = JIRAReader()
    #file = reader.get_file(input("Issue number: "))
    file = reader.get_file('BPMPEF-1906')
    inst_creator = InstructionCreator(file,reader.get_option())
    inst_creator.generate_instructions(inst_creator.opt.get('system','source_type'))

if __name__ == '__main__':
    run()