from collections import defaultdict 
import heapq
import math

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w])
        
    def Dijkstra(self, s): 
        s = str(s)
        graph_dict = self.get_graph_dict()
        if not graph_dict:
            return

        pri_queue = list()
        history = set()

        heapq.heappush(pri_queue, (0, s))

        combine = {s: None}
        distance = self.get_distance(graph_dict, s)

        while len(pri_queue) > 0:
            pair = heapq.heappop(pri_queue)
            span = pair[0]
            vertex = pair[1]
            history.add(vertex)

            path_list = graph_dict[vertex].keys()
            for path in path_list:
                if path not in history:
                    new_dist = span + graph_dict[vertex][path]
                    if new_dist < distance[path]:
                        heapq.heappush(pri_queue, (new_dist, path))
                        combine[path] = vertex
                        distance[path] = new_dist

        return distance

    def get_graph_dict(self) -> dict:
        if len(self.graph) == 0:
            return

        result = {}
        for point in range(len(self.graph)):
            path_list = self.graph[point]

            data = {}
            for other, span in enumerate(path_list):
                if other == point or span == 0:
                    continue
                data[str(other)] = span

            result[str(point)] = data

        return result

    def get_distance(self, graph_dict: dict, s: str):
        result = {s: 0}
        for vertex in graph_dict.keys():
            if vertex != s:
                result[vertex] = math.inf
        return result

    def Kruskal(self):
        MST = {}
        for node in range(len(self.pair)):
            self.weight = self.sortset(self.pair[node][0], self.pair[node][1])
        
        for edge in range(len(list(self.weight.keys()))):
            node1 = list(self.weight.keys())[edge][0]
            node2 = list(self.weight.keys())[edge][1]

            node1_setidx = self.find_index(node1)
            node2_setidx = self.find_index(node2)
            
            len_node1_set = len(self.set[node1_setidx])
            len_node2_set = len(self.set[node2_setidx])           
            if len_node1_set >= len_node2_set:
                if node2 not in self.set[node1_setidx]:
                    self.set[node1_setidx] += self.set[node2_setidx]
                    self.set[node2_setidx] = []
                    MST.setdefault(list(self.weight.keys())[edge], list(self.weight.values())[edge])
            else:
                if node1 not in self.set[node2_setidx]:
                    self.set[node2_setidx] += self.set[node1_setidx]
                    self.set[node1_setidx] = []
                    MST.setdefault(list(self.weight.keys())[edge], list(self.weight.values())[edge])                    
        Kruskal_dict = self.transform(MST)
        return Kruskal_dict
