# Simplest Path

class Graph(object):
    
    def __init__(self, graph_dict={}):
        self.graphDicitionary = graph_dict
        
    def vertices(self):
        return list(self.graphDicitionary.keys())
    
    def generateEdges(self):
        edges = []
        for vertex in self.graphDicitionary:
            print("vertex = ", vertex)
            for neighbour in self.graphDicitionary[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
                    return edges
                
    def checkForPath(self, source, destination, path = []):
        graph = self.graphDicitionary
        path = path + [source]
        if source == destination:
            return path
        if source not in graph:
            return None
        for vertex in graph[source]:
            if vertex not in path:
                extendedPath = self.checkForPath(vertex, destination, path)
                if extendedPath:
                    return extendedPath
                
        return None
    
if __name__=="__main__":
    
    g={
        "a":["c"],
        "b":["c","e"],
        "c":["a","b","d","e"],
        "d":["c"],
        "e":["c","b"],
        "f":[]
        }
    graph = Graph(g)
    print("vertices f graph")
    print(graph.vertices())
    print("edges of graph")
    print(graph.generateEdges())
    pathResult = graph.checkForPath("a","d")
    
    if (pathResult == None):
        print("Result1: No path Between source and destination")
    else:
        print("pathResult1:", pathResult)
        
    pathResult = graph.checkForPath("a","f")
    
    if (pathResult == None):
        print("Result1: No path Between source and destination")
    else:
        print("pathResult1:", pathResult)
    
    pathResult = graph.checkForPath("a", "e")
    
    if (pathResult == None):
        print("Result1: No path Between source and destination")
    else:
        print("pathResult1:", pathResult)
        
    pathResult = graph.checkForPath("a", "c")
    
    if (pathResult == None):
        print("Result1: No path Between source and destination")
    else:
        print("pathResult1:",pathResult)

'''
Output:
>>>
vertices f graph
['a', 'c', 'b', 'e', 'd', 'f']
edges of graph
vertex = a
[{'a', 'c'}]
pathResult1: ['a', 'c', 'd']
Result1: No path Between source and destination
pathResult1: ['a', 'c', 'b', 'e']
pathResult1: ['a', 'c']
'''
