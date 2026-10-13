import csv


#1
def ex1(path):
    with open(path, 'r',encoding="utf-8") as f:
        content = f.read()
        len = 0
        for item in content:
            if(item == ' '):
              len += 1
    return len+1


print(ex1('a.txt'))

#2
def ex2(list):
    with open('data.csv','w',newline='') as c:
        writer = csv.writer(c)
        writer.writerow(["firstName", "lastName","age","city"])
        for item in list:
            writer.writerow(item)

list =[
    ["rivki","himmlfarb","19","modiin ilit"],
    ["sara", "levi", "15", "elad"],
    ["chani", "choen", "10", "jerusalem"]
]

ex2(list)

import json

#3
def ex3(dict):
    with open ("DATA.json",'w' ) as j:
        json.dump(dict,j)
    with open("DATA.json",'r') as j:
        print(j.read())


dict={
    "name": "rivki",
    "age":19,
    "city":"modi'in ilit"
}

ex3(dict)