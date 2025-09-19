class Student:
    def  __init__(self,marks , name , roll):
        self.name = name
        self.roll=roll
        self.marks=marks
    
    def display_info(self):
        print(f"my name is { self.name} , my roll number is {self.roll} and i got {self.marks} marks")


    def is_pass(self):
        if self.marks > 40:
            print("ya u have passed")
        else:
            print("na u havent passed")



s1 = Student(86,"goutham", 500 )
s1.display_info()
s1.is_pass()