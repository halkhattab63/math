# قم بعمل مخطط تدفقي يقوم بجمع الأعداد من 1 إلى 100 ويطبع قيمة المجموع للمستخدم.
# ( الحلول الرياضية ممنوعة:))


def sumto100():
    result = 0 
    for i in range(100 + 1):
        result = result +i 
    print(result)
# sum()

# هنا قمنا بجمع الاعداد بستخدام القانون العدد مضافا له واحد مقسوم على 2 
def sumToNumber(number ):
    # number = int(input("please Enter a number to add from zero to this number "))
    result = 0 
    result = (number * (number + 1)) / 2 

    print("the result of the addition is = ", result)
# number = 40
# sumToNumber(number)


def sumEvenNum10To100():
    result = 0 
    for i in range(10, 1000+1):
        if i%2 == 0 : 
            result = result + i 
    print(result)

sumEvenNum10To100()

def sumEvem(start, end):
    #  // استخدمنا هذه لانه عدد الحدود نريد عدد صحيح
    numberOfTerms = (end - start ) //2 + 1 
    sum = (end + start) /2 * numberOfTerms 
    
    print(sum)

start = 10
end = 1000 

sumEvem(start, end)