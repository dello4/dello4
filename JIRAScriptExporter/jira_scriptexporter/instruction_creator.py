'''
Created on 25/mar/2016

@author: Andrea Dell'Orto
'''
import csv
import os
import sys

from utility.script_validator import ScriptValidator
from utility.finder import Finder

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
        self.is_validation_enabled = self.opt.get('system','validate')
        
    def copy_model(self):
        out_file = open("istruzioni.txt", "a")
        with open(self.opt.get('system', 'model_name'), 'r') as model_file:
            for line in model_file:
                out_file.write(line)
        model_file.close()
        out_file.close()

    def generate_txt_file(self,out_path,out_file,root_to_search_in):
        if self.is_relative_enabled:
            out_path = out_path.replace(root_to_search_in,'.\\')
            out_file.writelines('\t' + out_path + '\n')  
    
    def generate_from_csv(self, validate):
        with open(self.file) as csvfile:
            delimiter = self.opt.get('script', 'split_separator')
            reader = csv.reader(csvfile, delimiter=delimiter, quotechar='\'')
            index = 0
            script_list = []
            out_file = open("istruzioni.txt", "a")
            for rows in reader:
                while index < len(rows):
                    root_to_search_in = self.opt.get('system','root_find')
                    finder1 = Finder()
                    out_path = finder1.find(rows[index],root_to_search_in)
                    if self.is_validation_enabled:
                        script_list.append(out_path)
                        self.generate_txt_file(out_path,out_file,root_to_search_in)
                    else: self.generate_txt_file(out_path,out_file,root_to_search_in)
                    index +=1
                    print("Writing line {0} of {1}".format(index, len(rows)))
            print("Instructions file created.\n Starting script validation:...")
            val = ScriptValidator(self.opt, self)
            if val.validate(script_list) :
                out_file.close()
                os.remove(out_file)
            else:
                out_file.close()
    
    def generate_instructions(self, source_type, validation):
        if self.opt.get('system', 'model'):
            self.copy_model()
        if self.case_csv == source_type:
            self.generate_from_csv(self.opt.get('system', 'validate'))
        elif self.case_txt == source_type:
            pass
        else:
            print("No valid value for source_type in JIRAExporter.cfg !!!")
        print("Saving instruction file.")
        print("File {0} saved.".format(self.opt.get('script', 'inst_filename')))
        sys.exit(2)
            
