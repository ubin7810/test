result1=0
result2=0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2


print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

class Calculator:
    def __init__(self):
        self.result=0
    def add(self,num):
        self.result += num
        return self.result

cal1=Calculator()
cal2=Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

def sub(self,num):
    self.result -= num
    return self.result

class FourCal:
    def setdata(self, first, second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def div(self):
        result=self.first/self.second
        return result

a=FourCal()
b=FourCal()
a.setdata(4,2)
b.setdata(3,8)
a.add()
a.mul()
a.sub()
a.div()
b.add()
b.mul()
b.sub()
b.div()
