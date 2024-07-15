import os 

try:
    file_name = 'motto.txt'
    file_1_handle = open(file_name,'w')
    file_1_handle.write('Fiat Lux!\n')
    file_1_handle.close()

finally:
    file_1_handle = open(file_name,'r+')
    line_1 = file_1_handle.read()
    print(line_1)
    file_1_handle.write('Let there be light!\n')
    file_1_handle.seek(0)
    result = file_1_handle.read()
    print(result)