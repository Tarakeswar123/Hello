'''
Created on 02-Jun-2020

@author: USER
'''
import xlrd
import xlwt
import logging
from exercise15.emptyfileexception import EmptyFileException
class LoadData(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def load_data_to_database(self,connection9):
        service_file=xlrd.open_workbook("service.xls")
        Sheet=service_file.sheet_by_index(0)
        rejection_file=xlwt.Workbook("rejectionfile.xls")
        rejection_sheet=rejection_file.add_sheet("sheet1")
        rejection_row=0
        rejection_sheet.write(rejection_row,0,"ServiceId")
        rejection_sheet.write(rejection_row,1,"ServiceDescription")
        rejection_sheet.write(rejection_row,2,"ServicePrice")
        read_counter=0
        insert_counter=0         
        if Sheet.nrows==0:
                raise EmptyFileException("The Selected File was empty")
        else:        
            for index in range(1,Sheet.nrows):
                serviceid=Sheet.cell(index,0).value
                servicedescription=Sheet.cell(index,1).value
                price=Sheet.cell(index,2).value
                read_counter=read_counter+1
                if price>0:
                    cursor=connection9.cursor()
                    cursor.execute("INSERT INTO service(service_id,service_description,price) VALUES(%s,%s,%s)",(str(serviceid),servicedescription,str(price)))
                    connection9.commit()
                    insert_counter=insert_counter+1
                else:
                    rejection_row=rejection_row+1
                    rejection_sheet.write(rejection_row,0,serviceid)
                    rejection_sheet.write(rejection_row,1,servicedescription)
                    rejection_sheet.write(rejection_row,2,price)
                    rejection_file.save("rejectionfile.xls")
            logger=logging.getLogger("logger")
            logger.setLevel(logging.INFO)
            file_handler=logging.FileHandler("logcounter.log","a")
            formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s : %(message)s")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
            logger.info("readcounter "+str(read_counter)+" insertcounter "+str(insert_counter))        
                