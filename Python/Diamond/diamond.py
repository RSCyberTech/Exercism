def rows(letter):
    letters=[chr(x) for x in range(65,ord(letter)+1)]
    
    toRet=[]
    for r in range(len(letters)):
        toAp=''
        toAp+=' '*(len(letters)-(len(toRet)+1))
        toAp+=letters[r]
        toAp+=' '*(len(letters)-len(toAp))
        toAp+=''.join(list(reversed(toAp[:-1])))
        toRet.append(toAp)
    if len(toRet)-1:
        toRet+=list(reversed(toRet[:-1]))
        
    return toRet
