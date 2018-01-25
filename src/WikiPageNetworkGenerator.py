import pandas as pd
import networkx as nx
from NetworkUtils import NetworkUtils


class Test(object):
    

    def main():
        input_path  = "C:\\Users\\Vinay\\Desktop\\Unstructured Data Analysis\\Semantic Network Analysis\\Data\\Wiki Essays Views Network Data.csv"
        network     = NetworkUtils()
        df          = pd.DataFrame.from_csv(input_path)
        authors       = set()   
        pages       = set()       
        G = nx.Graph()
        nodeColDict = {}
        
        for index, row in df.iterrows():
            if(row['PageId'] not in pages):
                (G,nodeColDict) = network.addNode(G,'Page',str(row['PageId'])+'p',nodeColDict)
                pages.add(row['PageId'])
                
            if(row['AuthorId'] not in authors):
                (G,nodeColDict) = network.addNode(G,'Author',str(row['AuthorId'])+'a',nodeColDict)
                authors.add(row['AuthorId'])
                
            G = network.addEdge(G,str(row['PageId'])+'p',str(row['AuthorId'])+'a')
    
        
        network.visualize(G,nodeColDict)
        print(nx.info(G))
    
    
    if __name__ == "__main__":
        main()
        
        

    