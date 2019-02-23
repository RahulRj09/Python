m = [1, 2, [3, 4, [5, 6, [7, 8]], 9, 10], 11, 12]

def flat_list(a_list):
    b_list = []
    for a in a_list:
        if type(a) != int:
            b_list = b_list + flat_list(a)
        else:
            b_list.append(a)
            
    return b_list
print(flat_list(m))