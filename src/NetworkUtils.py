import networkx as nx
import matplotlib.pyplot as plt

class NetworkUtils:
    
    
        #Adds the node color to the dictionary, adds node to graph, and returns both network and color dictionary
        def addNode(self,G,nodeType,nodeId,nodeColDict):
            color1=0.8 #red
            color2=0.0 #blue
            
            if nodeType is 'Page':
                nodeColDict[nodeId]=color1
            elif nodeType is 'Author':
                nodeColDict[nodeId]=color2
                
            G.add_node(nodeId)
            return(G,nodeColDict)
                
        #Adds an edge        
        def addEdge(self,G,source,dest):
            G.add_edge(source,dest)
            return G
         
       #visualizes network, given the color dictionary to allow different node colors          
        def visualize(self,G,valMap):
            values = [valMap.get(node) for node in G.nodes()]
            nx.draw(G, node_size=12, with_labels=False, width=0.1,  node_color=values)
            plt.show()
