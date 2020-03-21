class Bird:
    pass


bird = Bird()
setattr(bird, "wingspan", 42)  # can pass func too! to dynamically set at runtime
print(bird.wingspan)

print(getattr(bird, "wingspan"))

print(type(Bird))
print(Bird.__class__)
print(type(Bird.__class__))
print(type(Bird.__class__).__class__)
print((Bird.__class__).__class__)
print(type(bird))

# type() is Pythons God Object! Everything is built from type, like ruby Object
# types function signature: type(class_name, parents[tuple], attributes[dict])
# type is a metaclass
# metaclasses are classes that generate classes

# how python creates objects:
# does this class have a metaclass on it? yes - use it to create object
# traverse up chain of parents to root object to do the same

# a metaclass is any callable (function or class) that implements types
# function signature, for example:
# DON'T DO THIS, USE CLASSES
def my_meta_class(class_name, class_parents, class_attrs):
    # ... create more classes, add attrs to class on the fly,
    # create funcs dynamically, traverse parent class, change values in class, etc..

    # type() creates the class not  the instance! cookie cutters not cookies
    return type(class_name, class_parents, class_attrs)  # let python create class


# type here indicates a metaclass
# DO THIS, unless you absolutely need the function version (i.e.. class based views django)
class MyMetaClass(type):
    # new creates, init initializes
    def __new__(klass, class_name, class_parents, class_attrs):  # override callable
        # ... create more classes, add attrs to class on the fly,
        # create funcs dynamically, traverse parent class, change values in class, etc..
        return type.__new__(klass, class_name, class_parents, class_attrs)


# if this class has metaclass, set MyMetaClass to the callable class for object
class Myclass:
    __metaclass__ = MyMetaClass


UltraClass = MyMetaClass("Myclass", (), {})

# Rules:
# 1. don't use metaclasses (unless have to)
# 2. if building complicated dynamic API, use them
# 3. Make your metaclass a class not a function, derive from type
