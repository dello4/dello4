'''
Created on 25/mar/2016

@author: Andrea Dell'Orto
'''
import csv

class InstructionCreator(object):
    '''
    This class creates a .txt file based on the dictionary containing the classpaths.
    '''

    def __init__(self, file, opt):
        '''
        Constructor
        '''
        self.file = file
        self.opt = opt
    
    def generate_instructions(self):
        # for rec in self.file:
        #    pass
        with open(self.file) as csvfile:
            delimiter = self.opt.get('script', 'split_separator')
            reader = csv.reader(csvfile, delimiter=delimiter, quotechar='|')
            out_file = open("istruzioni.txt", "a")
            for row in reader:
                lines = str(row).split(delimiter)
                for line in lines:
                    out_file.write(line)
            out_file.close()
