import mysql.connector
#pip3 install mysql-connector-python
def getConnection():
    connection = mysql.connector.connect(host='localhost', 
                                        user='root', 
                                        passwd='Mynew113',
                                        database='Quan_ly_hoc_vien'
    )
    return connection