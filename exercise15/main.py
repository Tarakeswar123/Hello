'''
Created on 02-Jun-2020

@author: USER
'''
from exercise15.connectionusingxml import DBConnectionUsingxml
from exercise15.loaddata import LoadData
connection9=DBConnectionUsingxml().connect_to_the_database()
LoadData().load_data_to_database(connection9)