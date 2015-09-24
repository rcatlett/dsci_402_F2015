#Import Way 1
#from first_module import add_2
#print(add_2(10,8))

#Import Way 2
#import first_module
#print(first_module.add_2(5,6))

#Import Way 3
#import first_module as fm
#print(fm.add_2(3,4))

# print(fm.add_2(10,15, mult_by = 3))
# print(fm.add_2(10,15, 3))

from first_module import *
optional_args_test(1,2,3,4,5)

#using list as arguments
data = [1,3]
print (add_2(*data))

nums = range(-10, 11)
print(my_filter(lambda x: x > 0, nums))

print(sum_range(0,1))

print(factorial(5))

print(fib(1,1,10))
