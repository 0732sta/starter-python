#no need identify or name, anonymous function

nums=[1,2,3,4,5,6]

#def square(n):
#    return n*n

def square(nums):
    return nums*nums

print(list(map(square,nums)))
print(list(map(lambda n:n*n,nums)))