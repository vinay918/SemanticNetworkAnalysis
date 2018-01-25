import mysql.connector as sql
import pandas as pd

#Object to handle database interactions
class DatabaseAbstractionLayer:
    
    host=''
    database=''
    user=''
    pasword=''
    
    #constructor. Connects and creates the object
    def __init__(self,host,database,user,password):
        self.host     = host
        self.database = database
        self.user = user
        self.password = password 
        self.db_connection = sql.connect(host=self.host, database=self.database, user=self.user, password=self.password)
    
    #executes a query and returns a pandas DataFrame
    def executeQuery(self,query):
        df = pd.read_sql(query, con=self.db_connection)
        return df
        #df.to_csv('C:\Users\Vinay\Desktop\out.csv', index=False)
        
    
        

