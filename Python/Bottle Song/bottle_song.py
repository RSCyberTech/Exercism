def recite(start, take=1):

    numbers = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10:'ten'
    }
    
    toRet=[]
    for t in range(take):
        if start>1:
            toRet.append(f"{numbers[start].capitalize()} green bottles hanging on the wall,")
            toRet.append(f"{numbers[start].capitalize()} green bottles hanging on the wall,")
            toRet.append(f"And if one green bottle should accidentally fall,")
            start-=1
            if start>1:    
                toRet.append(f"There'll be {numbers[start]} green bottles hanging on the wall.")
            elif start>0:                
                toRet.append(f"There'll be {numbers[start]} green bottle hanging on the wall.")
        else:
            toRet.append(f"{numbers[start].capitalize()} green bottle hanging on the wall,")
            toRet.append(f"{numbers[start].capitalize()} green bottle hanging on the wall,")
            toRet.append(f"And if one green bottle should accidentally fall,")
            start-=1
            toRet.append("There'll be no green bottles hanging on the wall.")
            break
        if t+1 < take:
            toRet.append("")

    return toRet