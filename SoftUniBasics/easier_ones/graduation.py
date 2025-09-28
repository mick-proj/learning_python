name = str(input())
grade = 0
grade_counter = 0
failed_times = 0

while True:
    if grade_counter == 12:
        print(f'{name} graduated. Average grade: {(grade/12):.2f}')
    annual_grade = float(input())
    if annual_grade < 4:
        failed_times += 1
        if failed_times > 1:
            print(f'{name} has been excluded at {grade_counter}th grade')
            break
        continue
    grade_counter +=1
    grade += annual_grade

