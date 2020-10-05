import collections 
import heapq
import data

Connection = collections.namedtuple('Connection', 'cost path')

class Heap(object):
    # min heap
    def __init__(self):
        self._values = [] 

    def push(self, value):
        heapq.heappush(self._values, value)
    
    def pop(self):
        return heapq.heappop(self._values)
    
    def __len__(self):
        return len(self._values)

    def display(self):
        print("DISPLAYING")
        print(self._values)
        print(" ")

class Dijkstra():
    def __init__(self):
        self._neighbors = collections.defaultdict(set)
    def create(self, start, end, cost):
        self._neighbors[start].add((end, cost))

    def graph(self):
        print("-----------CURRENT GRAPH-----------")
        print(self._neighbors)
        print(" ")
    
    def neighbors(self, node):
        yield from self._neighbors[node]

    def search(self, origin, destination):
        routes = Heap()

        for neighbor in self.neighbors(origin):
            cost = neighbor[1]
            routes.push(Connection(cost = cost,  path = [origin, neighbor[0]]))

        visited = set()
        visited.add(origin)

        while routes:
            #routes.display()
            cost, path = routes.pop()
            current = path[-1]

            print("Current node: {0} Current cost: {1} Path: {2}".format(current, cost, path))
            
            if current in visited:
                continue 
            
            if current is destination:
                print("DONE")
                print("path:", path)
                print("distance:", cost)
                return cost, path 
            
            for neighbor in self.neighbors(current):
                if neighbor not in visited:
                    new_cost = cost + neighbor[1] 
                    new_path = path + [neighbor[0]]
                    routes.push((Connection(new_cost, new_path)))
            
            visited.add(current)
            
            print("visited: ", visited)
            print(" ")
            

        return "UNABLE TO DETERMINE"


def create_graph(dijk):
    for key in data.edges.keys():
        for j in range(len(data.edges[key][1])):
            if j != key:
                dijk.create(key, j, data.edges[key][1][j][0])

def main():
    dijk = Dijkstra()
    create_graph(dijk)
    dijk.search(15, 56)

main()




