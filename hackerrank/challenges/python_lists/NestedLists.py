student_dic = {}
for _ in range(int(input())):
    Name = input()
    Grade = float(input())
    student_dic[Name] = Grade

second = sorted(list(set(student_dic.values())))[1]
second_lowest = []  # 8
for stud_name, stud_mark in student_dic.items():
    if stud_mark == second:
        second_lowest.append(stud_name)
second_lowest.sort()  # 12
for name in second_lowest:
    print(name)
