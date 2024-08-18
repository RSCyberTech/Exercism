def find_anagrams(word, candidates):
    toRet=[]
    for c in candidates:
        if len(c) != len(word):
            continue
        
        toAdd=c
        for char in word:
            c=c.lower().replace(char.lower(),'',1)
            print(c)
        
        if c=='' and word.lower()!=toAdd.lower():
            toRet.append(toAdd)

    return toRet