from datetime import datetime


def decorator(func):
    def wapper(*args, **kwars):
        start = datetime.now()
        result = func(*args, **kwars)
        print(datetime.now() - start)
        return result
    return wapper

@decorator
def zadacha(args, k):
    
    otvet = []
    
    for i in range(len(args)):
        for j in range(len(args) - 1):
            
            if args[i] + args[j + 1] == k:
                otvet.append([args[i], args[j + 1]])
    return otvet[0]

print(zadacha([1,2,3,4,5,6], 7))

@decorator
def zadacha_(args, k):
    for i in range(len(args)-2):
        for j in range(i + 1, len(args)):
            if args[i] + args[j] == k:
                return [args[i], args[j]]



print(zadacha_([1,2,3,4,5,6], 7))

