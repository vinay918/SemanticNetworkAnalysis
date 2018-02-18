import pandas as pd
import networkx as nx
from NetworkUtils import NetworkUtils


class Test(object):
    

    def main():
        input_path  = "C:\Users\Vinay\Desktop\Unstructured Data Analysis\Semantic Network Analysis\Data\Essays\Fall 2012\Processed2\Wiki Analysis CSCE 155A view.csv"
        network     = NetworkUtils()
        df          = pd.DataFrame.from_csv(input_path)
        df_instructors = pd.DataFrame.from_csv("C:\\Users\\Vinay\\Desktop\\Unstructured Data Analysis\\Semantic Network Analysis\\Data\\Instructors\\instructors.csv")
        authors       = set() 
        instructors = set()  
        pages       = set()       
        G = nx.Graph()
        nodeColDict = {}
        count = 0
        edgeDict = dict()
        
        #Adding all instructor user ids to a set
        for index, row in df_instructors.iterrows():
            instructors.add(row['UserId'])
        
        #Iterating to keep track of edge weights and to add nodes to network
        for index, row in df.iterrows():
            
            #Keeping track of edge weights in a dictionary
            if(str(row['PageId'])+";"+str(row['AuthorId']) in edgeDict.keys()):
                edgeDict[str(row['PageId'])+";"+str(row['AuthorId'])] = edgeDict.get(str(row['PageId'])+";"+str(row['AuthorId'])) + 1
            elif(row['AuthorId'] not in instructors):
                edgeDict[str(row['PageId'])+";"+str(row['AuthorId'])] = 1            
            
            #adding page nodes to network if not already in the network
            if(row['PageId'] not in pages):
                (G,nodeColDict) = network.addNode(G,'Page',str(row['PageId'])+'p',nodeColDict)
                pages.add(row['PageId'])
                count = count + 1
            
            # Adding author nodes if not already in the network and if not an instructor        
            if(row['AuthorId'] not in authors and row['AuthorId'] not in instructors):
                (G,nodeColDict) = network.addNode(G,'Author',str(row['AuthorId'])+'a',nodeColDict)
                authors.add(row['AuthorId'])
                count = count + 1
            
            #FOR UNWEIGHTED EDGES, uncomment this line and comment out line 50
            #G = network.addEdge(G,str(row['PageId'])+'p',str(row['AuthorId'])+'a')
        
        #Add weighted edges to network        
        G = network.addWeightedEdges(G,edgeDict)

        #print "Cluster Coeff:"
        #print nx.average_clustering(G)
        #print nx.info(G)
        #print "Avg Node Connectivity:"
        #print nx.average_node_connectivity(G)

        
        #visualize the network
        network.visualize(G,nodeColDict,pages)
        
    
    if __name__ == "__main__":
        main()
        
        

    
