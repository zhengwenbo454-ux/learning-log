students = [("Tom", 78), ("Jerry", 92), ("Mike", 65), ("Amy", 88)]
'''1. 按成绩排序'''
def sort_students(students):
    result = sorted(students, key=lambda x: x[1], reverse=True)
    return result
result = sort_students(students)

'''2. 按姓名排序'''
def sort_students_by_name(students):
    result = map(lambda x: x[0], sorted(students, key=lambda x: x[0]))
    return list(result)

'''3. 按成绩分组'''
def students_score_more_than_80(students):
    result = filter(lambda x: x[1] > 80, students)
    return list(result)


a = ["apple", "banana", "cherry"]
b = ["red", "yellow", "dark red"]
def zip_lists(a, b):
    result = zip(a, b)
    return list(result)

'''4. enumerate函数'''
def enumerate_list(lst):
    result = enumerate(lst)
    return list(result)


'''5. any/all函数'''
def check_students_pass(students):
    any_result = any(x[1] >= 90 for x in students)
    all_result = all(x[1] >= 90 for x in students)
    return any_result, all_result
print(check_students_pass(students))
