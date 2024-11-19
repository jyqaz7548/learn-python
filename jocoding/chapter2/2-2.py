a = "I ate %d apples" %3
b = "I ate %s apples" %"five"
print(a)
print(b)

number = 10
day = "three"
sen = "I ate {0} apples. so I was sick for {1} days" .format (number ,day)
print(sen)

c = "i eat {0} apples".format(3)
print(c)


name = '기모'
age = '30'
d = f'나의 이름은 {name+"딱"}입니다. 나이는 {age}입니다.'
print(d)
print(d.replace("나의 이름은","너의 이름은"))

e = "sssssssssdsssssss"
print(e.find('d'))

f = "," .join('doidmf')
print(f)

a ="hi"
print(a.upper())