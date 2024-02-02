def is_pangram(sentence):
    abc = list("abcdefghijklmnopqrstuvwxyz")
    for a in abc:
        if a not in sentence.lower():
            return False
    return True
