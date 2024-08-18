def commands(binary_str):
    codes={
        '00001':'wink',
        '00010':'double blink',
        '00100':'close your eyes',
        '01000':'jump',
        '10000':'Reverse the order of the operations in the secret handshake.',
    }

    toRet=[]
    for k,v in codes.items():
        if (int(k,2) & int(binary_str,2)) == int('10000',2):
            toRet.reverse()
        elif (int(k,2) & int(binary_str,2)) == int(k,2):
            toRet.append(v)

    return toRet