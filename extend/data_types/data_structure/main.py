# dynamic type
var_name = 1
var_name = True
type(var_name) # get type of the var
bool(var_name) # convert to boll (error here)
id(var_name) # get the memory address of the var

print(id(var_name))
second = var_name
print(id(second)) # same memory address

# func names
def get_name():
     # here we started with verb/action and the context
     return True