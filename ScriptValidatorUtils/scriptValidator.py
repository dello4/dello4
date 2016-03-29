# coding=utf-8

import os, re
import configparser
import inspect

def quotesRemover(quotedString):
 stringWithoutQuotes = quotedString.replace('"', '')
 return stringWithoutQuotes
 
#Input directory for the script is read from file
cfgFilePath = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '\JIRAExporter.cfg'
config = configparser.ConfigParser()
config.readfp(open(cfgFilePath))

isDebug = config.getboolean('sys','isDebug')
isError = False

if config.has_section('dir'):
    inputdir = config.get('dir','input')

    for file in os.listdir(inputdir):
        #Only sql files
        if file.endswith(".sql"):
            file = os.path.join(inputdir,file)
            script = open(file)
            scriptAsString = script.read().lower()
            logname = 'spool &path.&nomeschema._'+os.path.splitext(os.path.basename(script.name))[0]+'.log\n'
            
			#Loading base elements from the configuration file
            strings = [logname.lower()]
            for (each_key, each_val) in config.items('base_elements'):
                strings.append(quotesRemover(each_val))
            if isDebug: print(strings)
			#Errors list loaded from config file
            errorsList = []
            for (each_key, each_val) in config.items('errors'):
                errorsList.append(quotesRemover(each_val))
            if isDebug: print(errorsList)
			#Verify the script
			#Lowercase conversion of the entire script to perform statement analisys
            if all(s.lower() in scriptAsString for s in strings) and not any(s.lower() in scriptAsString for s in errorsList):
                print("Script " + os.path.basename(script.name) + " è verificato.")
            else:
                print("ERR02: Lo script " + file + " non rispetta lo standard!! - Non è presente o è scritto male ")
                script.close()
                isError = True
                break
            script.close()
    if not isError:
        print("Tutti gli script sembrano essere coerenti!")
else:
    print("ERR01 - File di configurazione non trovato.")

input("Press any key to exit...")