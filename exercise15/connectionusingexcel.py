'''
Created on 02-Jun-2020

@author: USER
'''
import xlrd
import psycopg2
from xlrd.sheet import Sheet
class DBConnectionUsingExcel(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def connect_to_the_database_excel(self):
        connection_file=xlrd.open_workbook("connection_config.xls")
        Sheet=connection_file.sheet_by_index(0)
        for index in range(1,Sheet.nrows):
            dbname=Sheet.cell(index,0).value
            username=Sheet.cell(index,1).value
            server=Sheet.cell(index,2).value
            password=str(Sheet.cell(index,3).value)
            print("Password which was retrieved from excel",password)
            #This was done due to the password to connect to database is a number
            password9=""
            for index in range(0,len(password)-2,1):
                password9=password9+password[index]
            print("Original password after conversion is",password9)
            connection9=psycopg2.connect("dbname='"+dbname+"' user='"+username+"' host='"+server+"' password='"+password9+"'")
            print("Database connection has been established")
            print(connection9)
            return connection9
             
               