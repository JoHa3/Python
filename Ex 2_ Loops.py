import math 
n = int(input ("input positive number1, "))
m = int(input ("input positive number2, "))
if n == 0 or m == 0 :
    print("Enter a positive number greater than 0")
else :
     greatest_common_divisor =  math.gcd(n, m)
     print(f"The greatest common divisor of {n} and {m} is: {greatest_common_divisor}")