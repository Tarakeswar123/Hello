'''
Created on 02-Jun-2020

@author: USER
'''

class EmptyFileException(Exception):
    '''
    classdocs
    '''


    def __init__(self, message):
        '''
        Constructor
        '''
        self.message=message
        
    def __str__(self):
        return self.message
            