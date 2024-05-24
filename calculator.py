# switchقم بعمل برنامج آلة حاسبة بسيطة باستخدام ال 
#  حيث تقوم بقراءة العملية وعددين من المستخدم وتقوم بتطبيق العملية المرادة وفقاً لما يدخله المستخدم.
# (15إذا أدخل المستخدم العملية + على سبيل المثال وأخل العددين 10 و 
#  سيتم عمل جمع لكلا العددين ومن ثم طباعة  الناتج)


def calculate(x , y ,z ):
    
    match z :
        case '+' : 
            return x + y 
        case '-' :
            return x - y 
        case '/' : 
            if y != 0:
                return x / y
            else:
                return "Cannot divide by zero"
        case '*' : 
            return x * y
        case '**' : 
            return x ** y 
        case '//' :
            return x//y  
        case '%' : 
            return x % y
        case _:
            return "Invalid operation" 
        
def print_calculate():
    result = 0  
    while True : 
        try :
                number1 = float(input("Please enter a number : "))
                number2 = float(input("Please enter a number : "))
                operation = input("Please enter a operation : " ).strip()  
                result = calculate(number1 , number2 , operation)
                print(f"{number1} {operation} {number2} = {result}")

        except ValueError:
            print("Please enter valid numbers.")

        another_calculation = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if another_calculation != 'yes' :
            print("Exiting the calculator. Goodbye!")
            break
# Call the function to start the calculator
print_calculate()




# def calculate(expression):
#     try:
#         # تقييم التعبير الرياضي المدخل من قبل المستخدم
#         result = eval(expression)
#         return result
#     except ZeroDivisionError:
#         return "Error: Division by zero is not allowed."
#     except Exception as e:
#         return f"Error: Invalid input ({e})"

# def print_calculate():
#     print("Welcome to the Calculator!")
#     print("Enter a mathematical expression (or 'exit' to quit).")
    
#     while True:
#         # طلب التعبير الرياضي من المستخدم
#         expression = input("Expression: ")
        
#         if expression.lower() == 'exit':
#             print("Exiting the calculator. Goodbye!")
#             break
        
#         # حساب النتيجة
#         result = calculate(expression)
        
#         # طباعة النتيجة
#         print(f"Result: {result}")

# # Call the function to start the calculator
# # print_calculate()

# import tkinter as tk

# def calculate(expression):
#     try:
#         # تقييم التعبير الرياضي المدخل من قبل المستخدم
#         result = eval(expression)
#         return result
#     except ZeroDivisionError:
#         return "Error: Division by zero is not allowed."
#     except Exception as e:
#         return f"Error: Invalid input ({e})"

# def on_submit():
#     # الحصول على التعبير المدخل من المستخدم
#     expression = entry.get()
    
#     # حساب النتيجة
#     result = calculate(expression)
    
#     # عرض النتيجة في العلامة
#     label_result.config(text=f"Result: {result}")

# # إنشاء نافذة tkinter
# root = tk.Tk()
# root.title("Calculator")

# # إنشاء مربع نصي وعلامة لعرض النتيجة
# entry = tk.Entry(root, width=50)
# label_result = tk.Label(root, text="Result: ")

# # زر لتقديم التعبير
# button_submit = tk.Button(root, text="Submit", command=on_submit)

# # تحديد مواقع المكونات في النافذة
# entry.pack(pady=10)
# button_submit.pack(pady=5)
# label_result.pack(pady=10)

# # تشغيل البرنامج
# root.mainloop()
