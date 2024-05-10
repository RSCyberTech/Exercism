def rotate(text, key):
    text=list(text)
    for r in range(len(text)):
        if (65 <= ord(text[r]) <= 90):
            t=ord(text[r])+key if ord(text[r])+key<=90 else 64+(ord(text[r])+key-90)
        elif (97 <= ord(text[r]) <= 122):
            t=ord(text[r])+key if ord(text[r])+key<=122 else 96+(ord(text[r])+key-122)
        if t:
            text[r]=chr(t)
            t=None
    return ''.join(text)
