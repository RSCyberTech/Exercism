def spiral_matrix(size):
    matrix=[[0 for c in range(size)] for r in range(size)]
    
    locations=[]
    modifier=0
    while len(locations)!=(size**2):
        row=modifier
        for r in range(row,row+1):
            for c in range(size):
                if (r,c) not in locations:
                    locations.append((r,c))
        col=size-1-modifier
        for r in range(size):
            for c in range(col,col-1,-1):
                if (r,c) not in locations:
                    locations.append((r,c))
        row=size-1-modifier
        for r in range(row,row-1,-1):
            for c in range(size-1,-1,-1):
                if (r,c) not in locations:
                    locations.append((r,c))
        col=modifier
        for r in range(size-1,-1,-1):
            for c in range(col,col+1):
                if (r,c) not in locations:
                    locations.append((r,c))
        modifier+=1
    
    for l in range(len(locations)):
        toWork=locations.pop(0)
        matrix[toWork[0]][toWork[1]]=(size**2)-len(locations)
        
    return matrix