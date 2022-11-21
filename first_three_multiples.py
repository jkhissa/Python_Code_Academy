def first_three_multiples(num):
    for x in range(1,4):
        print(num*x)
        if x == 3:
            return num*3

first_three_multiples(10)