from DatabaseAbstractionLayer import DatabaseAbstractionLayer
import pandas as pd

def main():
    
# Edit database and path information here. The input path is required to read in PageIds of interest. 
    output_path="C:\Users\Vinay\Desktop\Unstructured Data Analysis\Semantic Network Analysis\Data\Essays\Fall 2015\Processed2\\"
    input_path="C:\Users\Vinay\Desktop\Unstructured Data Analysis\Semantic Network Analysis\Data\Essays\Fall 2015\CSCE 155N.csv"    
    
    database=DatabaseAbstractionLayer("?","?","?","?")
    
    #extractInstructors(output_path,database)
    #extractNetwork(database,input_path,output_path,"comment")
    extractNetwork(database,input_path,output_path,'view')
   # extractNetwork(database,input_path,output_path,'edit')
    
    
 # Uses query, updates PageId to extract necessary database entries, and updates dataframe. Remember to update line 33 for desired file name  
def extractNetwork(database,input_path,output_path,condition):
    query="select wt.AuthorId,wt.UserAction,wt.PageId,wt.ActionTimestamp,w.Id from wikitracking wt join wikipage w on wt.PageId = w.PageId WHERE w.Id="   
    queryComplete = "Group by wt.Id;"
    df=pd.DataFrame()
    df_wikiIds=pd.DataFrame.from_csv(input_path)
    i=0;
    rows=len(df_wikiIds.index)
    
    for index, row in df_wikiIds.iterrows():
        query2=query+str(row['ID'])+" AND wt.UserAction like '%"+condition+"%' " + queryComplete + ";"
        df=df.append(database.executeQuery(query2))
        i=i+1
        print("Progress = "+str(i*100/rows)+" %")
    
    output_path=output_path+"Wiki Analysis CSCE 155N "+condition+".csv"        
    df.to_csv(output_path, index=True, encoding='utf-8-sig')

#Runs query to extract list of TAs and instructors
def extractInstructors(output_path,database):
    query="select DISTINCT(UserId) from wikigroupmembership WHERE Type like '%Admin%' or Type like '%Guest%';"
    df = pd.DataFrame()
    df = database.executeQuery(query)
    df.to_csv(output_path, index=True)      
    
if __name__ == "__main__":
    main()
