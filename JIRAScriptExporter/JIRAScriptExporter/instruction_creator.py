'''
Created on 25/mar/2016

@author: Andrea Dell'Orto
'''
import csv
import io


class InstructionCreator(object):
    '''
    This class creates a .txt file based on the dictionary containing the classpaths.
    '''


    def __init__(self, file):
        '''
        Constructor
        '''
        self.file = file
    
    def generate_instructions(self):
        #for rec in self.file:
        #    pass
        csv_file = open(self.file)
        csv_reader = csv.reader(csv_file)
        print(list(csv_reader))