money = True
if money:
    print("부자")
else :
    print("거지")


x =3
y= 2
print(x>y)

money = 2000
card = True

if money >= 3000 and card :
    print("택시를 타고가라")
else:
    print("걸어가라")

print(1 in [1,2,3])


print("p " in 'python')


pocket = ['paper','cellphone']
card = True

if 'money' in pocket :print("택시")

elif 'paper' not in pocket :print("택시를 타고가라")

else :
    print("걸어가라")


score = 100

message = "good" if score >= 60 else "fail"
print(message)