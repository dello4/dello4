'''
Created on 25/mar/2016

@author: Andrea Dell'Orto
'''
import csv
import sys
from tempfile import NamedTemporaryFile

from jira import JIRA

from jira_scriptexporter.config_reader import ConfigFileReader


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
                print("Connecting to {0}".format(jira_options['server']))
                jira = JIRA(options=jira_options, basic_auth=(self.opt.get('jira', 'jira_user'), self.opt.get('jira', 'jira_password')))
                print("Connection established")
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
                    '''
                    Using a temporary file to store data from the attachment
                    '''
                    print("Downloading file {0}".format(att.filename))
                    tfile = NamedTemporaryFile('wb', delete=False)
                    tfile.write(att.get())
                    return tfile.name
            else:
                print("Unexpected error: there's no \'script\' section in cfg file!")
        else:
            print("ERROR: No file named " + self.conf.get('script', 'file_name') + " were found!")
    
    def get_option(self):
        return self.opt
    
    def read_csv_file(self, file_to_open, delimiter):
        '''
        This method returns a list of strings contained in a CSV file with a given separator
        '''
        with open(file_to_open) as file:
            csv_file = csv.reader(file, delimiter=delimiter, quotechar='\'')
            csv_to_list = []
            index = 0
            for rows in csv_file:
                while index < len(rows):
                    csv_to_list.append(rows[index])
                    index +=1
            return csv_to_list
