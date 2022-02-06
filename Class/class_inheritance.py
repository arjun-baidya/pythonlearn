# Inheritance allows us to define a class that inherits all the methods and properties from another class. Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class.

# The Python super() method lets you access methods from a parent class from within a child class. This helps reduce repetition in your code. super() does not accept any arguments. One core feature of object-oriented programming languages like Python is inheritance.

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greetPerson(self):
        print("Hello " + self.name)
        print("Your age is " , self.age)


class Patient(Person):
    # def __init__(self, name, age, doctor):
    #     super().__init__(name, age)
    #     self.doctor = doctor
    # def greetPerson(self):
    #     super().greetPerson()
    #     print("Your doctor is " + self.doctor)
    def __init__(self, name, age, doctor):
        Person.__init__(self,name,age)
        self.doctor = doctor
    def print_doc(self):
        print("Your doctor is " + self.doctor)
    
    

patient_object = Patient("John", 36, "Dr. Smith")
patient_object.greetPerson()
patient_object.print_doc()
