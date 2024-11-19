a= [1,2,3]
b = a[:]
a[1] = 4    
print(a)
print(b)

a,b =("python",'is fun')
print(a)
print(b)

a = b = 'python'

a= 3
b= 5
a,b = b,a
print(a)
print(b)