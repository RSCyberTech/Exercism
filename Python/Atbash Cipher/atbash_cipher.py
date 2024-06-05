def encode(plain_text):
    letters=list('abcdefghijklmnopqrstuvwxyz')
    reverseLetters=list(reversed(letters))
    plain_text=plain_text.replace(' ','').replace(',','').replace('.','')
    toRet=''
    for p in plain_text:
        if len(toRet.replace(' ',''))%5==0 and len(toRet)>0:
            toRet+=' '
        if p.lower() in letters:
            toRet+=reverseLetters[letters.index(p.lower())]
        else:
            toRet+=p
    
    return str(toRet)
def decode(ciphered_text):
    return encode(ciphered_text).replace(' ','')