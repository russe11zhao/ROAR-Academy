import numpy as np

a1 = np.array([[1,2],[2,3]])
print(a1)
print(type(a1))

def swap_rows(M,a,b):
    if type(M) != np.ndarray or type(a) != int or type(b) != int:
        raise TypeError
    if M.shape[0] < 2 or M.shape[1] < 1:
        raise ValueError
    if a < 0 or b < 0:
        raise ValueError
    M[[a,b]] = M[[b,a]]

def swap_cols(M,a,b):
    if type(M) != np.ndarray or type(a) != int or type(b) != int:
        raise TypeError
    if M.shape[0] < 1 or M.shape[1] < 2:
        raise ValueError
    if a < 0 or b < 0:
        raise ValueError
    M[:,[a,b]] = M[:,[b,a]]
    
swap_rows(a1,0,1)
print(a1)
swap_cols(a1,0,1)
print(a1)