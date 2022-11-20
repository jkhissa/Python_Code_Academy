# def delete_starting_evens(lst):
#   while (len(lst) > 0 and lst[0] % 2 == 0):
#     lst = lst[1:]
#   return lst


# print(delete_starting_evens([2,4,5,2,5,6,2,3,2]))

#Odd indices program
# def odd_indices(lst):
#     new_lst = []
#     for item in lst:
#         if len(lst) > 0 and lst.index(item) > 0 and lst.index(item) % 2 != 0:
#             new_lst.append(item)
#     return new_lst

# print(odd_indices([4, 3, 7, 10, 11, -2]))

#exponents

# def exponents(bases, powers):
#     new_lst = []
#     for item in bases:
#         for index in powers:
#             new_item = item ** index
#             new_lst.append(new_item)
    
#     return new_lst
        
# print(exponents([2, 3, 4], [1, 2, 3]))


# def same_values(lst1, lst2):
#   new_lst = []
#   for index in range(len(lst1)):
#     if lst1[index] == lst2[index]:
#       new_lst.append(index)
#   return new_lst
# print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


# def tenth_power(num):
#     return num**10

# def square_root(num):
#     return num ** 0.5

# def win_percentage(wins, losses):
#     return (wins/(wins+losses)) * 100
# print(win_percentage(10, 0))


# def average(num1, num2):
#     return (num1+num2)/2

# def remainder(num1, num2):
#     return ((num1*2)%(num2*0.5))

def first_three_multiples(num):
    for x in range(1,4):
        print(num*x)
        if x == 3:
            return num*3

first_three_multiples(10)

def tip(total, percentage):
    decimal_percentage = percentage/100
    tip_amount = (total*decimal_percentage)
    return tip_amount

def introduction(first_name, last_name):
    print(last_name, ',' , first_name)  

def dog_years(name, age):
    dog_age = age*7
    return name + ", you are " + dog_age + "years old in dog years"