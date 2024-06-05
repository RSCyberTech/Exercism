def resistor_label(colors):
    codes={
        'Black':0,
        'Brown':1,
        'Red':2,
        'Orange':3,
        'Yellow':4,
        'Green':5,
        'Blue':6,
        'Violet':7,
        'Grey':8,
        'White':9,
    }
    tolerances={
        'Grey':0.05,
        'Violet':0.1,
        'Blue':0.25,
        'Green':0.5,
        'Brown':1,
        'Red':2,
        'Gold':5,
        'Silver':10,
    }
    if len(colors)==1:
        return str(codes[colors[0].capitalize()])+' ohms'
    
    toRet=''
    counter=len(colors)-2
    for c in colors[:counter]:
        toRet+=str(codes[c.capitalize()])
    if len(colors)>counter:
        toRet+='0'*codes[colors[counter].capitalize()]
    if codes[colors[counter].capitalize()]>6:
        number=int(toRet)/1000000000
        text=' gigaohms'
        toRet=(str(number) if str(number).endswith('0')==False else str(int(number)))+text
    elif codes[colors[counter].capitalize()]>3:
        number=int(toRet)/1000000
        text=' megaohms'
        toRet=(str(number) if str(number).endswith('0')==False else str(int(number)))+text
    elif codes[colors[counter].capitalize()]>0 and len(toRet)>3:
        number=int(toRet)/1000
        text=' kiloohms'
        toRet=(str(number) if str(number).endswith('0')==False else str(int(number)))+text
    else:
        toRet=str(int(toRet))+' ohms'
    toRet+=' ±{}%'.format(tolerances[colors[-1].capitalize()])
    print(toRet)
    
    return toRet