from collections import defaultdict

class graph:
    def __init__(self,vertices):
        self.v=vertices  #no of vertices
        self.graph=defaultdict(list)  #default dictionary

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def DFSutil(self,v,visited):
        visited[v]=True #mark as visited

        for i in self.graph[v]:
            if visited[i]==False:
                self.DFSutil(i,visited)
                
    def isconnected(self):
        visited=[False]*(self.v) #mark all not visited

        #find vertex with nonzero degree
        for i in range(self.v):
            if len(self.graph[i])>1:
                break

    #if there are no edges return true
        if i==self.v-1:
            return True

    #check if nonzero vertices
        for i in range(self.v):
            if visited[i]==False and len(self.graph[i])>0:
                return True


    def isEulerian(self):
        if self.isconnected()==False:
          return 0
        else:
            odd=0
            for i in range(self.v):
                if len(self.graph[i] )% 2 !=0:
                    odd +=1
                if odd==0:
                    return 2
                elif odd==2:
                    return 1
                elif odd>2:
                    return 0

    def test(self):
        res=self.isEulerian()
        if res==0:
            print("graph is not eulerian")


        elif res==1:
            print("graph has euler path")

        else:
            print("graph has euler cycle")

    
g1=graph(5)
g1.addEdge(0,1)
g1.addEdge(1,2)
g1.addEdge(2,3)
g1.addEdge(2,0)
g1.addEdge(3,4)

g1.test()
        
