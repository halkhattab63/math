# قم بعمل مخطط تدفقي يأخذ رقم من المستخدم ويطبع جدول الضرب الخاص به.
# (مثال : إذا أدخل المستخدم القيمة 5 فيكون الناتج .... 5 * 1 = 1 , 5 * 2 = 10 , 5 * 3 = 15 )

def multiplication_table(number):
    for i in range(20 +1 ): 
        print(f"{i} x {number} = " , i * number)


user_number = int(input("Please enter a number : "))
multiplication_table(user_number)