
#1
string = input('Enter a string: \n')
i = 0
while i < len(string):
    if string[i] != string[-i-1]:
        print("is not palindrome")
        break
    i = i + 1
if i == len(string):
     print("is palindrome")


#2
string = input('Enter a string: \n')
count = 1
for char in string:
    if char == ' ':
        count = count + 1
print(count)

#3
string = input('Enter a string: \n')
new_string = string[0]
i = 0
while i < len(string)-1:
    if string[i] == ' ':
        new_string = new_string + string[i+1]
    i = i + 1
print(new_string)

