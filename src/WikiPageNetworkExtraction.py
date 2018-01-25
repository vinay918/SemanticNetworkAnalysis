from DatabaseAbstractionLayer import DatabaseAbstractionLayer
import pandas as pd

def main():
    
# Edit database and path information here. The input path is required to read in PageIds of interest. 
    database=DatabaseAbstractionLayer("?","?","?","?")
    query="SELECT * FROM wikitracking WHERE PageId="
    output_path="C:\\Users\\Vinay\\Desktop\\Unstructured Data Analysis\\Semantic Network Analysis\\Data\\Wiki Essays Views Network Data.csv"
    input_path="C:\\Users\\Vinay\\Desktop\\Unstructured Data Analysis\\Semantic Network Analysis\\Data\\Wiki Group Essays Charts All v2.csv"
    
    df=pd.DataFrame()
    df_wikiIds=pd.DataFrame.from_csv(input_path)
    i=0;
    rows=len(df_wikiIds.index)
    
    for index, row in df_wikiIds.iterrows():
        query2=query+str(row['ID'])+" AND UserAction like '%comment%';"
        df=df.append(database.executeQuery(query2))
        i=i+1
        print("Progress = "+str(i*100/rows)+" %")
        
    df.to_csv(output_path, index=False)
    
    
if __name__ == "__main__":
    main()
