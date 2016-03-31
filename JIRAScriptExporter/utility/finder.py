'''
Created on 31/mar/2016

@author: Andrea Dell'Orto
'''
import os


class Finder(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def find(self,name, root):
        for path, dirs, files in os.walk(root):
            if name in files:
                return os.path.join(root, name)