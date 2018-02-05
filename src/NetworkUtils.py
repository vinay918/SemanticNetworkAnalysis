import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

class NetworkUtils:
    
    
        #Adds the node color to the dictionary, adds node to graph, and returns both network and color dictionary
        def addNode(self,G,nodeType,nodeId,nodeColDict):
            color1='r' #red page
            color2='b' #blue author
            
            if nodeType is 'Page':
                nodeColDict[nodeId]=color1
            elif nodeType is 'Author':
                nodeColDict[nodeId]=color2
                
            G.add_node(nodeId)
            return(G,nodeColDict)
                
        #Adds an edge for unweighted graphs       
        def addEdge(self,G,source,dest):
            G.add_edge(source,dest)
            return G       
         
         
       #visualizes network, given the color dictionary to allow different node colors          
        def visualize(self,G,valMap):
            values = [valMap.get(node) for node in G.nodes()]
            edgeCols = [G[u][v]['color'] for u,v in G.edges()]
            edges,weights = zip(*nx.get_edge_attributes(G,'weight').items())
            nx.draw(G, node_size=10, edge_color = edgeCols, with_labels=False, width=0.25, node_color=values)
            plt.show()
            return
        
        #Adds edges to a network and assigns a color to the edge depending on its weight
        def addWeightedEdges(self,G,edges):
            col1 = 'k'
            col2 = 'b'
            col3 = 'r'
            for key, value in edges.iteritems():
                nodes = key.split(';')
                if(value < 5):
                    G.add_edge(str(nodes[0]+'p'),str(nodes[1]+'a'),weight = value,color = col1)
                elif(value>=5 and value <10):
                    G.add_edge(str(nodes[0]+'p'),str(nodes[1]+'a'),weight = value, color = col2)
                else:
                    G.add_edge(str(nodes[0]+'p'),str(nodes[1]+'a'),weight = value, color = col3)                    
            return G
            
      # Used to keep track of the weight of edges (the number of occurences of a specific connection)  
        def weightDict(self,df):
            output = {}
            for index, row in df.iterrows():
                
                if(str(row['PageId'])+";"+str(row['AuthorId']) in output.keys()):
                    output[str(row['PageId'])+";"+str(row['AuthorId'])] = output.get(str(row['PageId'])+";"+str(row['AuthorId'])) + 1
                else:
                    output[str(row['PageId'])+";"+str(row['AuthorId'])] = 1
                    
            return output
