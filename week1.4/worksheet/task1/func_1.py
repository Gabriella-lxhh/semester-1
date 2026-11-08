
def func_1(lst_value): 
    ''' 
    write your docstring to explain the function 
        
Calculates and returns the mean of a non-empty list of numbers.

Args:
    lst_value (list): A non-empty list of numbers.

Returns:
    float: The mean of the numbers.
'''

    sum = 0 
    num_of_value = len(lst_value) 
    for value in lst_value: 
        sum = sum + value 
    return sum/num_of_value 
print(func_1([10, 20, 30]))