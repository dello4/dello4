'''
Created on 25/mar/2016

@author: Andrea Dell'Orto
'''
from JIRAScriptExporter import script_exporter
from jira import JIRA

class JIRAReader(object):
    '''
    Class who connects to JIRA and gest csv file
    '''
    
    conf = script_exporter.ConfigFileReader()

    def __init__(self, conf):
        self.conf = conf
        
    def connect(self):
        if self.conf.has_section('jira_url'):
            try:
                jira = JIRA(self.conf.get('jira_url', 'url'))
            except(ConnectionError, ConnectionRefusedError):
                print('Error connecting ' + self.conf.get('jira_url', 'url'))
