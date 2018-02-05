import pandas as pd
import networkx as nx
from NetworkUtils import NetworkUtils


class Test(object):
    

    def main():
        input_path  = "C:\Users\Vinay\Desktop\Unstructured Data Analysis\Semantic Network Analysis\Data\Essays\Fall 2015\Processed\Wiki Analysis CSCE 310 edit.csv"
        network     = NetworkUtils()
        df          = pd.DataFrame.from_csv(input_path)
        
        authors       = set()   
        pages       = set()       
        G = nx.Graph()
        nodeColDict = {}
        count = 0
        edgeDict = dict()
        
        #Iterating to keep track of edge weights and to add nodes to network
        for index, row in df.iterrows():
            
            #Keeping track of edge weights in a dictionary
            if(str(row['PageId'])+";"+str(row['AuthorId']) in edgeDict.keys()):
                edgeDict[str(row['PageId'])+";"+str(row['AuthorId'])] = edgeDict.get(str(row['PageId'])+";"+str(row['AuthorId'])) + 1
            else:
                edgeDict[str(row['PageId'])+";"+str(row['AuthorId'])] = 1            
            
            #adding nodes
            if(row['PageId'] not in pages):
                (G,nodeColDict) = network.addNode(G,'Page',str(row['PageId'])+'p',nodeColDict)
                pages.add(row['PageId'])
                count = count +1
                
            if(row['AuthorId'] not in authors):
                (G,nodeColDict) = network.addNode(G,'Author',str(row['AuthorId'])+'a',nodeColDict)
                authors.add(row['AuthorId'])
                count = count +1
            
            #FOR UNWEIGHTED EDGES, uncomment this line and comment out line 45
            #G = network.addEdge(G,str(row['PageId'])+'p',str(row['AuthorId'])+'a')
        
        #Add weighted edges to network        
        G = network.addWeightedEdges(G,edgeDict)
        
        #visualize the network
        network.visualize(G,nodeColDict)
        print(nx.info(G))
        
    
    if __name__ == "__main__":
        main()
        
        

    