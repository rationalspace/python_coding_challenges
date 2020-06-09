# Enter your age from command line and see if you are old or not 
class Person:
    def __init__(self,startAge):
        if(startAge>0):
            self.age = startAge
        else:
            print("Age entered is not valid - making it 0")
            self.age = 0

    def AmIOld(self):
        if(self.age>50):
            print("You are old")
        elif(self.age >= 13 and self.age < 18):
            print("You are a teenager")
        else:
            print("You are a child")

age = int(input("Please enter your age "))
p = Person(age)
p.AmIOld()