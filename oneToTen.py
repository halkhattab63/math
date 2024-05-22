# قم بعمل مخطط تدفقي يأخذ رقمين من المستخدم X و Y ويطبع جميع الأعداد الموجودة بين  X و Y .
# (إذا كان العددان المأخوذان من المستخدم 5 و 10 سيتم طباعة 6 7 8 9 على الترتيب)

def islem():
    x = int (input("Please Enter first number"))
    y = int (input("Please Enter second number"))

    if x < y : 
        for i in range(x + 1 , y ) :
            print(i)  
    else: 
        temp = x 
        x = y 
        y = temp 

        for i in range(x + 1 , y ) :
            print(i)  

islem()