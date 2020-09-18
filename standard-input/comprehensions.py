#double price money weekend bonanza
prices=[5, 10, 50, 100, 1000]

dbl_prices=[]
for price in prices:
    dbl_prices.append(price*2)
print(dbl_prices)

#comprehension method
dbl_prices=[price*2 for price in prices]
print(dbl_prices)

#squaring numbers
nums=[1,2,3,4,5,6,7,8,9,10]

squared_even_nums=[]
for num in nums:
    if(num**2)%2==0:
        squared_even_nums.append(num**2)
print(squared_even_nums)

#comprehension method
squared_even_nums=[num**2 for num in nums if (num**2)%2==0]
print(squared_even_nums)