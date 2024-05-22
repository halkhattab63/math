# قم بعمل مخطط تدفقي يأخذ رقم من المستخدم ويطبع إذا ما كان الرقم أولي أم غير أولي.
# (الرقم الأولي هو الرقم الذي يقبل القسمة على 1 وعلى نفسه فقط 
# أي أن باقي قسمته (المود) مع جميع الأرقام لا يساوي صفر)  


import math
import time
def is_prime(number):

    if number < 2 :
        return False 
    if number == 2 : 
        return True 
    if number %2 == 0 :
        return False 

    for i in range(3 , int (math.sqrt(number) + 1) ,2 ):
        if  number%i == 0 : 
            return False 
    return True  


start_time = time.time()
number = int(input("Please enter your number for checking if it's a prime number: "))

if is_prime(number):
    print(f"Your number is {number}\nThis number is a prime number.")
else:
    print(f"Your number is {number}\nThis number is not a prime number.")

end_time = time.time()
execution_time = end_time - start_time

print(f"Running time: {execution_time:.6f} seconds")

