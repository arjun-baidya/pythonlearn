# A class can be derived from more than one base class in Python, similar to C++. This is called multiple inheritance. In multiple inheritance, the features of all the base classes are inherited into the derived class. The syntax for multiple inheritance is similar to single inheritance.

class SampleBase1:
    def sampleBase1Function(self):
        print("SampleBase1")
    
class SampleBase2:
    def sampleBase2Function(self):
        print("SampleBase2")
class MultipleInheritance(SampleBase1,SampleBase2):
    pass

MultipleInheritanceObject = MultipleInheritance()
MultipleInheritanceObject.sampleBase1Function()
MultipleInheritanceObject.sampleBase2Function()

print(MultipleInheritanceObject.__class__.__bases__)

