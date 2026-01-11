# variable is used to a value
name = "Sulthan" # in this case Sulthan saving in variable name
print(name)

# if have variable with same name, the last variable will be use entire down code, the first one will be use until meet the second
name = "Rafi" 
print(name)

# len is used to count length variable
# example
print(len(name)) # Rafi -> 4 soo the output is 4

# and this is example how to use variable
length_name = len(name) # we save value len to a variable calling length_name
print("panjang variable nama adalah :",length_name) # so we can use the variable in feature print like this

# or we can make cool version, with input, len and print together
print(len(input("Hello what is your name : ")))