def append(list1, list2):
    list1 = list1 + list2
    return list1


def concat(lists):
    toRet = []
    for l in lists:
        toRet.extend(l)
    return toRet


def filter(function, list):
    result = []
    for l in list:
        if function(l):
            result.append(l)
    return result


def length(list):
    l = 0
    for li in list:
        l += 1
    return l


def map(function, list):
    result = []
    for l in list:
        result.append(function(l))
    return result


def foldl(function, list, initial):
    for l in list:
        initial = function(initial, l)
    return initial


def foldr(function, list, initial):
    for l in list[::-1]:
        initial = function(initial, l)
    return initial


def reverse(list):
    return list[::-1]
