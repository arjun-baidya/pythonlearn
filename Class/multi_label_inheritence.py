# The multi-level inheritance includes the involvement of at least two or more than two classes. One class inherits the features from a parent class and the newly created sub-class becomes the base class for another new class

class Lavel1:
    pass

class Lavel2(Lavel1):
    pass

class MultiLevelInheritance(Lavel2):
    pass

multilavelinheritanceObject = MultiLevelInheritance()
print(multilavelinheritanceObject.__class__.__bases__)
print(MultiLevelInheritance.__mro__)
print(MultiLevelInheritance.__bases__)