'''
Created on 25/mar/2016

@author: Andrea Dell'Orto
'''
import csv
import sys

from jira import JIRA

from JIRAScriptExporter.config_reader import ConfigFileReader


class JIRAReader(object):
    '''
    Class implementing a task reader for jira
    '''
    opt = ""

    def __init__(self):
        conf = ConfigFileReader()
        self.opt = conf.options

    def connect(self):
        if self.opt.has_section('jira'):
            try:
                jira_options = {'server': self.opt.get('jira', 'url')}
                jira = JIRA(options=jira_options, basic_auth=(self.opt.get('jira', 'jira_user'), self.opt.get('jira', 'jira_password')))
            except(ConnectionError, ConnectionRefusedError) as e:
                print('Error connecting to %1: ({0}) {1}' % self.opt.get('jira_url', 'url'), e.errno, e.strerror)
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
            if self.opt.has_section('script'):
                if self.opt.get('script', 'file_name') == att.filename:
                    out_file = open("temp.csv","wb")
                    out_file.write(att.get())
                    out_file.close()
                    return out_file
            else:
                print("Unexpected error: there's no \'script\' section in cfg file!")
        else:
            print("ERROR: No file named " + self.conf.get('script', 'file_name') + " were found!")
            
    def read_csv_file(self, file_to_open):
        '''
        This method returns a list of script contained in a CSV file
        '''
        #csv_file = csv.reader(open(file_to_open), delimiter = self.conf.get('script', 'split_separator'))
        with open(file_to_open, 'rb') as file:
            csv_file = file.read()
            return csv_file
        #scriptsAsString = csv_file.read().lower()
        #if self.opt.get('script', 'split_enabled'):
        #    scripts_list = scriptsAsString.split(self.conf.get('script', 'split_separator'))
        #    return scripts_list
        #return scriptsAsString
