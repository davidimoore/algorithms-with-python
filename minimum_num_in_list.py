def min_val_n(list):
    highest = list.pop(0)
    for n in list:
        if n > highest:
            highest = n
    return highest

list_of_num = [0,99,1,22,500,3]

print(min_val_n(list_of_num))

        
