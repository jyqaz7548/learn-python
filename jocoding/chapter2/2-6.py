s1 ={1,2,3}
print(type(s1))
s1 = set("Hello")
s2 = set("Hello World!")
print(s1&s2)
print(s1 | s2)
print(s1-s2)
print(s2-s1)
s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)
s1.remove(2)
print(s1)