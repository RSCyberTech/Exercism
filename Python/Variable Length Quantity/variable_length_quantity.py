def encode(numbers):
    toRet=[]
    for n in numbers:
        toWork=''
        toWork+=bin(n)[2:]
        while toWork:
            step=len(toWork)%7 if len(toWork)%7 > 0 else 7
            toRet.append(    int(    '1'+('0'*(7-len(toWork[:step])))+toWork[:step]    ,2)    )
            toWork=toWork[step:]
        toRet[-1]&=127
    return toRet
    
def decode(bytes_):
    toRet=['']
    complete=None
    while bytes_:
        complete=False
        toWork=bytes_.pop(0)
        toWork=bin(toWork)[2:]
        if len(toWork) != 8:
            toWork=('0'*(8-len(toWork)%8))+toWork
        if toWork.startswith('0'):
            toRet[-1]=int(toRet[-1]+toWork[1:],2)
            if len(bytes_):
                toRet.append('')
            else:
                complete=True
        else:
            toRet[-1]+=toWork[1:]
    if complete==True:
        return toRet 
    else:
        raise ValueError("incomplete sequence")