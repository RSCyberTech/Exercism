def annotate(minefield):
    locations=[
        (-1,-1),(-1,0),(-1,1),
        (0,-1),(0,1),
        (1,-1),(1,0),(1,1)
    ]
    check=len(minefield[0]) if len(minefield) > 0 else None
    for row in range(len(minefield)):
        if len(minefield[row]) != check:
            raise ValueError("The board is invalid with current input.") 
        minefield[row]=list(minefield[row])
        for space in range(len(minefield[row])):
            if minefield[row][space]!= '*':
                if minefield[row][space]!= ' ':
                    raise ValueError("The board is invalid with current input.") 
                mines=0
                for l in locations:
                    try:
                        if minefield[row+l[0]][space+l[1]]=='*' and row+l[0]>=0 and space+l[1]>=0:
                            mines+=1
                    except:
                        pass
                if mines != 0:
                    minefield[row][space]=str(mines)
        minefield[row]=''.join(minefield[row])
    return minefield