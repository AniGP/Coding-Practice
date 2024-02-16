import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    
    reverse_arr = numpy.array(arr, float)[::-1]
    
    return reverse_arr

arr = input().strip().split(' ')
result = arrays(arr)
print(result)