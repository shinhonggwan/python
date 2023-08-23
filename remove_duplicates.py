def distinct(seq):
    new_list = []
    for i in seq:
        if i in new_list:
            pass
        elif i not in new_list:
            new_list.append(i)
    return new_list

seq = [1, 1, 2]
print(distinct(seq))