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

    def __init__(self, config_read):
        conf = config_read
        self.opt = conf.options

    def _quotes_remover(self, quotedString):
        stringWithoutQuotes = quotedString.replace('"', '')
        return stringWithoutQuotes
    
    def validate(self):
        is_error = False
        is_debug = self.opt.getboolean('system','is_debug')
        if self.opt.has_section('system'):
            inputdir = self.opt.get('system','root_find')
            for file in os.listdir(inputdir):
                #Only sql files
                if file.endswith(".sql"):
                    file = os.path.join(inputdir,file)
                    script = open(file)
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
                        print("Script " + os.path.basename(script.name) + " è verificato.")
                    elif not is_script:
                        pass
                    else:
                        print("ERR02: Lo script " + file + " non rispetta lo standard!! - Non è presente o è scritto male ")
                        script.close()
                        is_error = True
                        break
                    script.close()
            if not is_error:
                print("Tutti gli script sembrano essere coerenti!")
        else:
            print("ERR01 - File di configurazione non trovato.")
            
