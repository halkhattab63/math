# لدى جامعة الفرات نظام للأقساط الجامعية يتم تحديده وفقاً لجنسية الطالب وعمره ويعمل بالشكل التالي
# : إذا كان الطالب تركياً لا يدفع أقساطاً جامعية أما إذا كان اجنبياً فيقوم الطالب بدفع 5000 ليرة إذا ما كان من جنسية أجنبية
#  (عدا السورية والعراقية) أما إذا كان سورياً أو عراقيا يقوم بدع نفس المبلغ إذا ما تجاوز عمره ال 30 سنة.

# قم بعمل برنامج يأخذ عُمر وجنسية الطالب ويطبع إذا ما كان عليه أن يدفع أقساطا جامعية       
#   أم لا وكم هو مبلغ هذا القسط إن وجد.

def tuition(nationality , age ):
    #{1:"turkish",2:"suriye",3:"iraq",4:"other"} 
    if nationality == 1 : 
        return f"You don't have to pay"
    
    elif nationality == 3 or nationality == 2:
        if age < 30 :
            return f"You don't have to pay"
        else :
            return f"You must pay the installments, which are 5,000 liras"
    
    elif nationality == 4  : 
        return f"You must pay the installments, which are 5,000 liras"

x = {1:"turkish",2:"suriye",3:"iraq",4:"other"} 

print("The following series represents the student's nationality. Please choose a number from the series")
for key , value in x.items(): 
    print(f"{key}:{value}")

user_input = input("Please enter your nationality ")
user_age = int (input("Please enter your age "))

try : 
    user_nationality = int(user_input)
    if user_nationality in x : 
        print( f"your nationality is : {user_nationality}")
        print(f"your age is : {user_age}")
        print(tuition(user_nationality,user_age))
    else :  
        print("The number you chose is not in the series.")

except ValueError:
    print("Please enter a valid number")

