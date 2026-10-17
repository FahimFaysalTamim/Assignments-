import heapq

def astar_search():
    HeuristicValue = {}  
    NeighborNode = {} 
    
    
    with open(r'C:\Users\Tamim\Downloads\CSE_422\Assignment_1\cities_2.txt', 'r') as file:

        for i in file :
            spaceLessLine = i.strip().split()  
            HeuristicValue[spaceLessLine[0]] = int(spaceLessLine[1]) 
            
            childNodes = []
            for j in range(2,len(spaceLessLine),2):
                 childNodes.append((spaceLessLine[j],int(spaceLessLine[j+1])))
            
            NeighborNode[spaceLessLine[0]] = childNodes
        
    


    
    start = input('Start : ').strip()
    Destination = input('Destination : ').strip()
    
    heap = []
    heapq.heappush(heap,(0+HeuristicValue[start],0,start,[]))
    

    visited = set()

    while heap : 
        f,goal,current,path = heapq.heappop(heap)
        
        

        if current in visited:
            continue 

        path = path + [current]
        
        visited.add(current)

        if current == Destination:
            if path:
              print("\nPath:", " -> ".join(path))
              print("Total Distance:", goal, "km")
            else:
              print("\nNO PATH FOUND") 
        
        for neighbor, cost in NeighborNode.get(current,[]):
            
            
            if neighbor not in visited:
                new_g = cost + goal
                new_f = new_g + HeuristicValue[neighbor]
                heapq.heappush(heap,(new_f,new_g,neighbor,path))

    
astar_search() 