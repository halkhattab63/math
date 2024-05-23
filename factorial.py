# قم بعمل مخطط تدفقي يأخذ رقم من المستخدم ويطبع قيمة العاملي الخاصة به
# (مثال : إذا أدخل المستخدم القيمة 5 فيكون الناتج 120 )
#  120 = 2*3*4*5


#  (Recursive Method)
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

print(factorial_recursive(5))  


# (Iterative Method)
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_iterative(5)) 


# (Standard Library)
import math
def factorial_math(n):
    return math.factorial(n)

print(factorial_math(5))  

# (Dynamic Programming)
def factorial_dynamic(n):
    if n == 0:
        return 1
    factorials = [1] * (n + 1)
    for i in range(2, n + 1):
        factorials[i] = i * factorials[i - 1]
    return factorials[n]
print(factorial_dynamic(5))



# Memoization
from functools import lru_cache
@lru_cache(maxsize=None)
def factorial_memoization(n):
    if n == 0:
        return 1
    else:
        return n * factorial_memoization(n-1)
print(factorial_memoization(5))  

