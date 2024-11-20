f= open("C:/chapter4/새파일.txt","w",encoding="UTF-8")
for i in range(1,11):
    data = "%d번쨰 줄입니다.\n"%i
    f.write(data)
f.close()


f= open("C:/chapter4/새파일.txt","r",encoding="UTF-8")
while True :
    line = f.readline()
    if not line :
        break
    print(line)
f.close()