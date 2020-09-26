'''
Created on 02-Jun-2020

@author: USER
'''
import xml.etree.ElementTree as ET
import psycopg2
class DBConnectionUsingxml(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def connect_to_the_database(self):
        file=ET.parse("connection_config.xml")
        root=file.getroot()
        dbname=root.find("dbname").text
        server=root.find("server").text
        username=root.find("username").text
        password=root.find("password").text
        connection9=psycopg2.connect("dbname='"+dbname+"' user='"+username+"' host='"+server+"' password='"+password+"'")
        print(connection9)
        print("Database connection has been established")
        return connection9
        
                