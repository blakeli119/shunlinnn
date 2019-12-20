from collections import defaultdict 
 
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 
 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def BFS(self, s):
        """
        :type s: int
        :rtype: list
        """
        queue = [s]
        answer= []
        
        while queue:
            s=queue.pop(0)
            answer.append(s)
            for a in self.graph[s]:
                    if a not in answer:
                        queue.append(a)
        return answer

    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
        stack = [s]
        answer = []
        
        while stack:
            s = stack.pop()
            answer.append(s)
            for a in self.graph[s]:
                if a not in answer:
                        stack.append(a)   
        return answer
