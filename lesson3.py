#1
def inventory_summary(**kwargs):
     sum = 0
     for key,value in kwargs.items():
      sum += value[0]
     return sum



print (inventory_summary(tomato=(25,4.9),milk=(44,6.1),
                         bread=(12,5.8),choclate=(10,9.9)))

print()

#1.2- (מילון)
def inventory_summary2(d):
    sum = 0
    for key, value in d.items():
        sum += value[0]
    return sum

dict={
    "tomato": (25,4.9),
    "milk":(44,6.1),
    "bread":(12,5.8),
    "choclate":(10,9.9)
}

print(inventory_summary2(dict))
print()

#2
def print_args_kwargs(*args, **kwargs):
    for item in args:
        print (item)
    for k,v in kwargs.items():
        print (k, v)


print_args_kwargs(1,2,"rivki",45,tomato=(25,4.9),milk=(44,6.1),
                         bread=(12,5.8),choclate=(10,9.9))

#3
def find_student(dictionary,key):
    if dictionary.get(key):
        return dictionary.get(key)
    return "no details"

my_dict={
    "rivki":20,
    "chany": 18,
    "esty":12,
    "eli":5
}

print (find_student(my_dict,"eli"))