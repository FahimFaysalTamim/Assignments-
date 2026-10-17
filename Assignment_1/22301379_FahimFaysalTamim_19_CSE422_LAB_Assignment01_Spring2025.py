import heapq

def astar():
    H_Value = {}  
    N_Node = {} 
    
    
    with open(r'C:\Users\Tamim\Downloads\CSE_422\Assignment_1\cities_2.txt', 'r') as file:

        for i in file :
            space_less = i.strip().split()  
            H_Value[space_less[0]] = int(space_less[1]) 
            
            childNodes = []
            for j in range(2,len(space_less),2):
                 childNodes.append((space_less[j],int(space_less[j+1])))
            
            N_Node[space_less[0]] = childNodes
        
    


    
    start = input('Start : ').strip()
    Destination = input('Destination : ').strip()
    
    gather = []
    heapq.heappush(gather,(0+H_Value[start],0,start,[]))
    

    visit = set()

    while gather : 
        f,goal,current,path = heapq.heappop(gather)
        
        

        if current in visit:
            continue 

        path = path + [current]
        
        visit.add(current)

        if current == Destination:
            if path:
              print("\nPath:", " -> ".join(path))
              print("Total Distance:", goal, "km")
            else:
              print("\nNO PATH FOUND") 
        
        for neighbor, cost in N_Node.get(current,[]):
            
            
            if neighbor not in visit:
                new_g = cost + goal
                new_f = new_g + H_Value[neighbor]
                heapq.heappush(gather,(new_f,new_g,neighbor,path))

    
astar() 