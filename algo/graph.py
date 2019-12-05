class Graph:
	def __init__(self,graph_dict={}):
		self.graph_dictionary=graph_dict
		
	def vertices(self):
		return list(self.graph_dictionary.keys())
		
	def generateEdges(self):
		edges=[]
		for vertex in self.graph_dictionary:
			#print("vertex = ")
			for neighbour in self.graph_dictionary[vertex]:
				if {neighbour,vertex} not in edges:
					edges.append({vertex,neighbour})
					return edges
					
	def edges(self):
		return self.generateEdges()
		
	def addVertex(self,vertex):
		if vertex not in self.graph_dictionary:
			self.graph_dictionary[vertex]=[]
			
	def addEdge(self,edge):
		edge=set(edge)
		vertex1,vertex2=tuple(edge)
		if vertex1 in self.graph_dictionary:
			self.graph_dictionary[vertex1].append(vertex2)
		else:
			self.graph_dictionary[vertex1]=[vertex2]
			
			
			
	def checkForPath(self,source,destination,path=[]):
		graph=self.graph_dictionary
		path=path+[source]
		if source==destination:
			return path
		if source not in graph:
			return None
		for vertex in graph[source]:
			if  vertex not in path:
				extendedPath=self.checkForPath(vertex,destination,path)
				if extendedPath:
					return extendedPath
		return None
		
		
if __name__=="__main__":
	g = {
		"a":["c"],
		"b":["c","e"] ,
		"c":["a", "b", "d", "e"] ,
		"d":["c"] ,
		"e": ["c", "b"],
		"f":[]
	}
	
	graph=Graph(g)
	
	print("vertices : ",graph.vertices())
	print()
	print("edges : ",graph.edges())
	print()
	
	pathResult = graph.checkForPath("a", "b")
	if pathResult==None:
		print("No path")
		
	else:
		print("path is : ",pathResult)
	
	
	
	
	
	
	
	
	
	
