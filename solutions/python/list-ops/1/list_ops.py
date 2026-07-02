def append(list1, list2):
    
    for item in list2:
        list1.append(item)
    return list1


def concat(lists):
    result = []
    for list in lists:
        for digit in list:
            
            result.append(digit)
    return result


def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result.append(item)
    return result


def length(list):
    count = 0
    for item in list:
        count += 1
    return count
    
def map(function, list):
    result = []
    for item in list:
        number = function(item)
        result.append(number)
    return result


def foldl(function, list, initial):
    acc = initial
    for item in list:
     acc = function(acc, item)
    
    return acc
        


def foldr(function, list, initial):
    acc = initial
    for item in list[::-1]:
     acc = function(acc, item)
    
    return acc


def reverse(list):
    return list[::-1]
