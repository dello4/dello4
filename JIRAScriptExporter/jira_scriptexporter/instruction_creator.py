'''
Created on 25/mar/2016

@author: Andrea Dell'Orto
'''
import csv
import os
import sys


class InstructionCreator(object):
    '''
    This class creates a .txt file based on the dictionary containing the classpaths.
    '''
    case_csv = 'CSV'
    case_txt = 'TXT'

    def __init__(self, file, opt):
        '''
        Constructor
        '''
        self.file = file
        self.opt = opt
        self.is_relative_enabled = self.opt.get('system','relative')
        
    def _find(self,name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)
    
    def generate_instructions(self, source_type):
        if self.opt.get('system', 'model'):
            out_file = open("istruzioni.txt", "a")
            with open(self.opt.get('system', 'model_name'), 'r') as model_file:
                for line in model_file:
                    out_file.write(line)
            model_file.close()
        else:
            out_file = open("istruzioni.txt", "a")
        if self.case_csv == source_type:
            with open(self.file) as csvfile:
                delimiter = self.opt.get('script', 'split_separator')
                reader = csv.reader(csvfile, delimiter=delimiter, quotechar='\'')
                index = 0
                for rows in reader:
                    while index < len(rows):
                        root_to_find_in = self.opt.get('system','root_find')
                        out_path = self._find(rows[index],root_to_find_in)
                        if self.is_relative_enabled:
                            out_path = out_path.replace(root_to_find_in,'.\\')
                        out_file.writelines('\t' + out_path + '\n')
                        index +=1
                        print("Writing line {0} of {1}".format(index, len(rows)))
                print("Instructions file created.")
        elif self.case_txt == source_type:
            pass
        else:
            print("No valid value for source_type in JIRAExporter.cfg !!!")
        print("Saving instruction file.")
        out_file.close()
        print("File {0} saved.".format(out_file.name))
        sys.exit(2)
            
