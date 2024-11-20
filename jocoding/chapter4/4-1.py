def add(a,b) :   
    result = a+b 
    return result

print(add(2,3))


def say() :
    return "Hi"

a = say()

print(a)

def plus(a,b):
    print("%d, %d의 합은 %d입니다."%(a,b,a+b))
    return a+b
a= plus(1,2)
print(a)


def add_many(*args):
    result = 0
    for i in args :
        result = result + i
    return result
    
print(add_many(1,2,3,4,5))
