'''
Created on 25/mar/2016

@author: Andrea Dell'Orto
'''
import csv

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
        with open(self.file) as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            out_file = open("istruzioni.txt","a")
            for row in reader:
                for r in row.split():
                    out_file.write(str(r))
            out_file.close()