# قم بعمل مخطط تدفقي يأخذ رقم من المستخدم ويطبع إذا ما كان الرقم أولي أم غير أولي.
# (الرقم الأولي هو الرقم الذي يقبل القسمة على 1 وعلى نفسه فقط 
# أي أن باقي قسمته (المود) مع جميع الأرقام لا يساوي صفر)  
import math
def prime(number):
    if number < 2 : return False 
    if number == 2 : return True 
    if number %2 == 0 : return False 
    for i in range(3 , int (math.sqrt(number) + 1) ,2 ):
        if  number%i == 0 : return False 
    return True 



import time
def wew(num):
    number =num
    result = 0 
    factor = 1 
    for i in range(1, number):
        factor *=i 
    result = factor + 1 
    
    if result % number == 0 : print(f"a {number} is prime ")
    else : print(f"a {number } is not prime")
number = 232521


start_time = time.time()

# تشغيل الدالة wew
wew(number)

# التقاط وقت الانتهاء
end_time = time.time()

# حساب وقت التشغيل
execution_time = end_time - start_time

print(f"run time : {execution_time} ")
