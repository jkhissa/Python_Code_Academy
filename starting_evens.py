def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst
  
print(delete_starting_evens([2,4,5,2,5,6,2,3,2]))