def exponents(bases, powers):
    new_lst = []
    for item in bases:
        for index in powers:
            new_item = item ** index
            new_lst.append(new_item)
    
    return new_lst
        
print(exponents([2, 3, 4], [1, 2, 3]))