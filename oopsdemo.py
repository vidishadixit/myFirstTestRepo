class Calculator:
    # below is class variable
    num = 100

    # default constructor

    def __init__(self, a, b):
        print("This will be executed automatically as soon as object gets created for this class")
        self.firstnumber = a
        self.secondnumber = b

    def Addition(self):
        print("this is addition method in a class")
        return self.firstnumber + self.secondnumber

    def Substraction(self):
        print("this is subtraction method in a class")
        return self.firstnumber - self.secondnumber


obj = Calculator(2, 3)
print("Class Variable : ")
print(obj.num)
print(obj.Addition())
print(obj.Substraction())

obj1 = Calculator(205, 153)
print("Class Variable : ")
print(obj1.num)
print(obj1.Addition())
print(obj1.Substraction())
