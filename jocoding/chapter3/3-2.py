treeHit = 0
while treeHit < 10 :
    treeHit +=1
    print ("나무를%d번 찍었습니다."%treeHit)
    if treeHit == 10:
        print('나무 넘어감')

prompt = """
1. Add
2. Del
3. List
4. Quit
Enter number: """

num = 0
while num != 4 :
    print(prompt)
    num= int(input())
