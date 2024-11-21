class Calculator :
    def __init__(self):
        self.result = 0

    def add(self,num) :
        self.result += num
        return self.result
    

cal1 = Calculator()
cal2 = Calculator()


class FourCal :
    def setdata(self,first,second) :
        self.first = first
        self.second = second

a = FourCal()
b = FourCal()
a.setdata(1,3)
b.setdata(4,7)

print(a.first)
print(b.first)