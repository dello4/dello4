'''
Created on 25/mar/2016

@author: Andrea Dell'Orto
'''
import sys
from JIRAScriptExporter import script_exporter
from jira import JIRA

class JIRAReader(object):
    '''
    Class implementing a task reader for jira
    '''
    conf = script_exporter.ConfigFileReader()

    def __init__(self, conf):
        self.conf = conf
        
    def connect(self):
        if self.conf.has_section('jira'):
            try:
                jira_options = {'server': self.conf.get('jira', 'url')}
                jira = JIRA(options=jira_options, basic_auth=(self.conf.get('jira', 'jira_user'), self.conf.get('jira', 'jira_password')))
            except(ConnectionError, ConnectionRefusedError) as e:
                print('Error connecting to %1: ({0}) {1}' % self.conf.get('jira_url', 'url'), e.errno, e.strerror)
            except:
                print("Unexpected error:", sys.exc_info()[0])
                raise
        return jira

    def get_file(self, issue_id):
        '''
        This method returns a file of a given name, attached to a JIRA task 
        '''
        jira = self.connect()
        issue = jira.issue(issue_id)
        attach_list = issue.fields.attachment
        for att in attach_list:
            if self.conf.has_section('script'):
                if self.conf.get('script', 'file_name') == att.filename:
                    return att
            else:
                print("Unexpected error: there's no \'script\' section in cfg file!")
        else:
            print("ERROR: No file named " + self.conf.get('script', 'file_name') + " were found!")
            
    def read_csv_file(self, file_to_open):
        '''
        This method returns a list of script contained in a CSV file
        '''
        csv_file = open(file_to_open)
        scriptsAsString = csv_file.read().lower()
        if self.conf.get('script', 'split_enabled'):
            scripts_list = scriptsAsString.split(self.conf.get('script', 'split_separator'))
            return scripts_list
        return scriptsAsString
