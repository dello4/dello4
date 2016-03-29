'''
Created on 25/mar/2016

@author: Andrea Dell'Orto
'''
import sys
from JIRAScriptExporter import script_exporter
from jira import JIRA
from test.test_zipfile import get_files

class JIRAReader(object):
    '''
    Class who connects to JIRA and gest csv file
    '''
    
    conf = script_exporter.ConfigFileReader()

    def __init__(self, conf):
        self.conf = conf
        
    def connect(self):
        if self.conf.has_section('jira'):
            try:
                jira_options = {'server': self.conf.get('jira', 'url')}
                jira = JIRA(options=jira_options,basic_auth=(self.conf.get('jira', 'jira_user'), self.conf.get('jira', 'jira_password')))
            except(ConnectionError, ConnectionRefusedError) as e:
                print('Error connecting to %1: ({0}) {1}' % self.conf.get('jira_url', 'url'), e.errno, e.strerror)
            except:
                print("Unexpected error:", sys.exc_info()[0])
                raise
        return jira

    def get_files(self):
        jira = self.connect()
        issue = jira.issue("")
        attach_list = issue.fields.attachment
        for att in attach_list:
            if self.conf.has_section('script'):
                if self.conf.get('script', 'file_name') == att.filename:
                    return att

    def read_csv_file(self):
        csv_file = open(self.get_files())
        scriptsAsString = csv_file.read().lower()
        scripts_list = scriptsAsString.split[',']
        return scripts_list