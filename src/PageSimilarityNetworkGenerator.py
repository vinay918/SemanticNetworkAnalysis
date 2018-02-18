import pandas as pd
import networkx as nx
from NetworkUtils import NetworkUtils


class Generator(object):
    

    def main():
        input_path  = "C:\Users\Vinay\Desktop\Unstructured Data Analysis\Semantic Network Analysis\Data\Essays\Fall 2012\Processed2\Wiki Analysis CSCE 155A view.csv"
        network     = NetworkUtils()
        df          = pd.DataFrame.from_csv(input_path) 
        pages       = set()       
        G = nx.Graph()
        nodeColDict = {}
                
        #Iterating to keep track of edge weights and to add nodes to network
        for index, row in df.iterrows():         
            
            #adding nodes
            if(row['PageId'] not in pages):
                (G,nodeColDict) = network.addNode(G,'Page',str(row['PageId'])+'p',nodeColDict)
                pages.add(row['PageId'])
        
        (G,pageTitles) = network.addInterPageEdges(G,pages)
        #print "Cluster Coeff:"
        #print nx.average_clustering(G)
        #print nx.info(G)
        #print "Avg Node Connectivity:"
        #print nx.average_node_connectivity(G)

        
        #visualize the network. Also input page ids to label them on the network.
        network.visualize(G,nodeColDict,pages)
        for page in pageTitles:
            print page
        
    
    if __name__ == "__main__":
        main()