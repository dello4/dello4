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
    
    def find(self, name, path, ignore_list):
        for root, dirs, files in os.walk(path, topdown=True, onerror=None):
            try:
                dirs[:] = [d for d in dirs if not d[0] == '.' and d not in ignore_list]
                files[:] = [f for f in files if len(f) <= 255 and not f[0] == '.']
                if name.lower() in [name.lower() for name in files]:
                    return os.path.join(root, name)
                else:
                    pass
            except os.error as err:
                if self.onerror is not None:
                    self.onerror(err)
                    return