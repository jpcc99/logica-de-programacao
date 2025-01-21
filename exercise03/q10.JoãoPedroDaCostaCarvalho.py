test_answer_key = input("").split(" ")
students_qtty = int(input(""))
students_ans = []

for _ in range(students_qtty):
    ans = input("").split(" ")
    students_ans.append(ans)

achieved_students = 0


def calc_student_grade(test_answer_key, ans):
    aux = [1 if test_answer_key[i] == ans[i] else 0 for i in range(len(ans))]
    sum = 0
    for i in aux:
        sum += i
    return sum


student_grades = [
    calc_student_grade(test_answer_key, students_ans[i]) for i in range(students_qtty)
]

for i in range(len(student_grades)):
    grade = student_grades[i]
    print(f"Aluno#{i + 1}: {grade:.1f}")
    if grade > 6:
        achieved_students += 1


def get_achievement_percent(students_qtty, achieved_students):
    return (achieved_students * 100) / students_qtty


print(f"Aprovação: {get_achievement_percent(
    students_qtty, achieved_students)}%")
