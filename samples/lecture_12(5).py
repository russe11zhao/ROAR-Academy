import numpy as np

list_1 = [1, 2, 3, 4]
def set_array(L,rows,cols):
    if len(L) != rows*cols:
        raise ValueError
    if type(L) != list or type(rows) !=  int or type(cols) != int:
        raise TypeError
    result_list = list()
    for i in range(rows):
        list_sub = list()
        for c in range(cols):
            list_sub.append(list_1[c + i*cols])
        tuple_sub = tuple(list_sub)
        result_list.append(tuple_sub)
    result_arr = np.array(result_list)
    return result_arr

set_array(list_1,2,2)
print(set_array(list_1,2,2))