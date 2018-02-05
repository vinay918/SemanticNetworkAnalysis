from DatabaseAbstractionLayer import DatabaseAbstractionLayer
import pandas as pd

def main():
    
# Edit database and path information here. The input path is required to read in PageIds of interest. 
    output_path="C:\\Users\\Vinay\\Desktop\\Unstructured Data Analysis\\Semantic Network Analysis\\Data\\Essays\\Fall 2015\\Processed\\"
    input_path="C:\\Users\\Vinay\\Desktop\\Unstructured Data Analysis\\Semantic Network Analysis\\Data\\Essays\\Fall 2015\\CSCE 322.csv"    
    
    database=DatabaseAbstractionLayer("kaw.unl.edu","wiki","lmille","E11im1")
    query="SELECT * FROM wikitracking WHERE PageId="
    extractNetwork(database,input_path,output_path,query,"comment")
    extractNetwork(database,input_path,output_path,query,'view')
    extractNetwork(database,input_path,output_path,query,'edit')
    
    
 # Uses query, updates PageId to extract necessary database entries, and updates dataframe. Remember to update line 31 for desired file name  
def extractNetwork(database,input_path,output_path,query,condition):
        
    df=pd.DataFrame()
    df_wikiIds=pd.DataFrame.from_csv(input_path)
    i=0;
    rows=len(df_wikiIds.index)
    
    for index, row in df_wikiIds.iterrows():
        query2=query+str(row['ID'])+" AND UserAction like '%"+condition+"%';"
        df=df.append(database.executeQuery(query2))
        i=i+1
        print("Progress = "+str(i*100/rows)+" %")
    
    output_path=output_path+"Wiki Analysis CSCE 322 "+condition+".csv"        
    df.to_csv(output_path, index=False)
    
    
if __name__ == "__main__":
    main()
