class A:
    def __init__(self, x):
        self.x = x

my_config = A("abc")

print(hasattr(my_config, 'x')) 

print(getattr(my_config, 'z',"None"))
print(getattr(my_config, 'x',"None"))

setattr(my_config, 'x', 'xyz') #if x not present creates one
print(f"{my_config.x}")

delattr(my_config, "x")
print(hasattr(A, "x"))
