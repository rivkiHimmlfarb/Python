#1
def reverse_list(l):
    new_list = []
    for index in range(len(l)):
        new_list.append(l[-index - 1])
    return new_list


nums = [1, 2, 3, 4]
print(reverse_list(nums))

#2
def calculate_avarage(l):
    sum = 0
    for item in l:
        sum = sum + item
    return sum/len(l)

print(calculate_avarage(nums))

#3
def is_prime(num):
    for index in range(2, num):
        if num/index ==4:
            return False
    return True

print (is_prime(13))
