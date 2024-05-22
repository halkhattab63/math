# قم بأخذ علامة الامتحان النصفي والنهائي من المستخدم
#  واطبع إذا ما كان الطالب قد نجح في المادة أم لم ينجح
# (يجب للمحصلة أن تكون أكثر من خمسين حتى ينجح الطالب) 
# (المحصلة يمكن حسابها بأخذ المتوسط الحسابي لعلامة الامتحان النصفي والنهائي).

def  calculate_agno():
    courses = ['algorithm analysis','algorithm one ', 'crypto','math one ', 'web development'] 
    grades = [] 

    print("--------------------------midterm--------------------------")
    for course in courses: 
        midterm_score = float(input(f'Enter {course} midterm exam score ')) *0.4
        grades.append([midterm_score, None])

    print("--------------------------final--------------------------")
    to_remove = []
    for i, course in enumerate(courses)  : 
        final_score = float(input(f'Enter{course} final exam score '))
        if final_score >= 50 : 
            print("Congratulations, you have passed the subject")
            grades[i][1] = final_score*0.6
        else:
            print("Sorry, you did not succeed in the subject.")
            to_remove.append(i)

    for i in sorted(to_remove, reverse=True):
        grades.pop(i)
    midterm = [grade[0] for grade in grades]
    final = [grade[1] for grade in grades if grades[1] is not None]

    midterm_average = sum(midterm) / len(midterm) if midterm else 0
    final_average = sum(final)/len(final)if final else 0 

    agon_score = midterm_average + final_average

    print("------------------------AGNO--------------------------")
    print("your AGNO is = ", agon_score)

calculate_agno()