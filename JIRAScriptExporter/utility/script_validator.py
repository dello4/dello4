'''
Created on 25/mar/2016

@author: Andrea Dell'Orto
'''
import os

from tempfile import NamedTemporaryFile

class ScriptValidator(object):
    '''
    Class implementing various validators for SQL scripts
    '''
    errors = {"ERR01":"ERR01 - Configuration file not found",
              "ERR02":"ERR02: The file {0} retun an error - No such file or wrong syntax!!"}

    def __init__(self, config_read):
        conf = config_read
        self.opt = conf.options

    def _quotes_remover(self, quotedString):
        stringWithoutQuotes = quotedString.replace('"', '')
        return stringWithoutQuotes
    
    def get_script_from_pilot(self, scriptAsString):
            print(scriptAsString.split('@',1)[-1:])
    
    def validate(self, file_list):
        is_error = False
        if self.opt.has_section('system'):
            is_debug = self.opt.getboolean('system','is_debug')
            for file in file_list:
                #Only sql files
                if file.endswith(".sql"):
                    script = open(file, 'r')
                    scriptAsString = script.read().lower()
                    logname = 'spool &path.&nomeschema._'+os.path.splitext(os.path.basename(script.name))[0]+'.log\n'
                    #Loading base elements from the configuration file
                    strings = [logname.lower()]
                    for (each_key, each_val) in self.opt.items('base_elements'):
                        strings.append(self._quotes_remover(each_val))
                    if is_debug:
                        print(strings)
                    #Errors list loaded from config file
                    errorsList = []
                    for (each_key, each_val) in self.opt.items('errors'):
                        errorsList.append(self._quotes_remover(each_val))
                    if is_debug:
                        print(errorsList)
                    #Verify the script
                    #Lowercase conversion of the entire script to perform statement analisys
                    is_script = not "DEF NOMESCHEMA" in scriptAsString
                    if is_script and all(s.lower() in scriptAsString for s in strings) and not any(s.lower() in scriptAsString for s in errorsList):
                        print("Script {0} has been verified.".format(os.path.basename(script.name)))
                    elif not is_script:
                        self.get_script_from_pilot(scriptAsString)
                    else:
                        print(self.errors.get("ERR02").format(script.name))
                        script.close()
                        is_error = True
                        break
                    script.close()
            if not is_error:
                print("All scripts verified.")
        else:
            print(self.errors.get("ERR01"))
            
