import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from DatabaseAbstractionLayer import DatabaseAbstractionLayer
from WikiPageNLP import WikiNLP


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
         
         
       #visualizes network, given the color dictionary to allow different node colors. Also labels pages on networks         
        def visualize(self,G,valMap,pages):
            values = [valMap.get(node) for node in G.nodes()]
            edgeCols = [G[u][v]['color'] for u,v in G.edges()]
            edges,weights = zip(*nx.get_edge_attributes(G,'weight').items())
            pos = nx.spring_layout( G )
            nx.draw(G, pos=pos, node_size=16, edge_color = edgeCols, with_labels=False, width=0.2, node_color=values)
            labels = {}
            for node in G.nodes():
                    if "a" not in node.replace("p","") and int(node.replace("p","")) in pages:
                            labels[node]=node
            nx.draw_networkx_labels(G,pos=pos,labels=labels,font_color='k',font_size=8)                
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
            
        #Generates inter page edges, given a list of page Ids. Also returns a list of the pages used    
        def addInterPageEdges(self,G,pages):
            database=DatabaseAbstractionLayer("?","?","?","?")
            textProcessor = WikiNLP()
            edgeDict = {}
            pageTitles = set()
            query = "select w1.* from wikipage w1 left join wikipage w2 on w1.Id = w2.Id and w1.revisionId < w2.revisionId where w2.revisionId is null and w1.pageID in (select w.PageId from wikigroup g left join page p on g.Id=p.groupId left join wikipage w on p.Id=w.pageId where w.PageId="
            completeQuery = " group by w.Id);"
            processed =set()
            total = len(pages)** 2
            count = 0.0
            for page1 in pages:
                processed.add(page1)
                query1 = query + str(page1) + completeQuery
                df_1 = database.executeQuery(query1)
                df_1['Content'] = df_1['Content'].apply(lambda x: ''.join([" " if ord(i) < 32 or ord(i) > 126 else i for i in x]))
                df_1['Title'] = df_1['Title'].apply(lambda x: ''.join([" " if ord(i) < 32 or ord(i) > 126 else i for i in x]))
                for index, row in df_1.iterrows():
                        string1 = str(row['Content'])
                        pageTitles.add(textProcessor.cleanhtml(str(row['Title']))+" "+str(page1))               
                for page2 in pages:
                        if page2 not in processed:
                                query2 = query + str(page2) + completeQuery
                                df_2 = database.executeQuery(query2)
                                df_2['Content'] = df_2['Content'].apply(lambda x: ''.join([" " if ord(i) < 32 or ord(i) > 126 else i for i in x]))
                                df_2['Title'] = df_2['Title'].apply(lambda x: ''.join([" " if ord(i) < 32 or ord(i) > 126 else i for i in x]))                        
                                for index, row in df_2.iterrows():
                                        string2 = str(row['Content'])
                                        pageTitles.add(textProcessor.cleanhtml(str(row['Title']))+" "+str(page2))
                                similar = textProcessor.symsimilarity(string1,string2)
                                edgeDict[str(page1)+"p;"+str(page2)+"p"] = similar
                        count=count+1
                        print "Progress = "+str(count/total*100)+"%"
            G = self.processPageEdgeWeights(G,edgeDict)
            
            return (G,pageTitles)
            
        #To remove non-ascii characters from a string
        def strip_non_ascii(string):
                stripped = (c for c in string if 0 < ord(c) < 127)
                return ''.join(stripped)
        
        #Adds weighted edges to graphs using lookup dictionary 
        def processPageEdgeWeights(self,G,edgeDict):
                col1 = 'k'
                col2 = 'b'
                col3 = 'r'
                for key,value in edgeDict.iteritems():
                        pages = key.split(';')
                        if(value < 0.1 and value > 0):
                                G.add_edge(pages[0],pages[1],weight = value,color = col1)
                        elif(value>=0.1 and value < 0.3):
                                G.add_edge(pages[0],pages[1],weight = value, color = col2)
                        elif(value>=0.3 and value <= 1):
                                G.add_edge(pages[0],pages[1],weight = value, color = col3)                    
                return G       
