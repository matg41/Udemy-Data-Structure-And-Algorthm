class Graph:
    def __init__(self) -> None:
        self.adj_list = {}
    
    def print_graph(self):
        for vertex in self.adj_list:
            print (vertex, ": ", self.adj_list[vertex])
        print('\n')

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self,vertex, connect):
        if vertex not in self.adj_list:
            self.adj_list[vertex]=[]
        if type(connect) == list:
            for i in connect:
                if i in self.adj_list:
                    if i not in self.adj_list[vertex]:
                        self.adj_list[vertex].append(i)
                        self.adj_list[i].append(vertex)
                else:
                    self.adj_list[i]=[vertex]
                    self.adj_list[vertex].append(i)
        else :
            if connect in self.adj_list:
                if connect not in self.adj_list[vertex]:
                    self.adj_list[vertex].append(connect)
                    self.adj_list[connect].append(vertex)
            else:
                self.adj_list[connect]=[vertex]
                self.adj_list[vertex].append(connect)
        return True

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list[v2] and v2 in self.adj_list[v1]:
            self.adj_list[v2].remove(v1)
            self.adj_list[v1].remove(v2)
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for i in self.adj_list[vertex]:
                self.adj_list[i].remove(vertex)
            self.adj_list.pop(vertex,None)
            return True
        return False

my_graph = Graph()

my_graph.add_vertex('A')
my_graph.add_vertex('B')
my_graph.add_vertex('C')
my_graph.add_edge('A',['B','C',])
my_graph.add_edge('B',['A','C','D'])
my_graph.add_edge('C','D')
my_graph.print_graph()
my_graph.remove_vertex('A')
my_graph.print_graph()


