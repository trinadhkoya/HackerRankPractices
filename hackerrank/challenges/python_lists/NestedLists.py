# create an empty student_dictionary
student_dic = {}
# iterate over given condition Ex:5
for _ in range(int(input())):
    # studnet name
    Name = input()
    # student mark
    Grade = float(input())
    # pushing the marks for respective student
    student_dic[Name] = Grade

'''access the values from student_dic,avod duplicates
by make use of set,and turn  it into lista and make them sorted
get the second position:we need the second lowest mark,as we have sorted
the post position is first low value store it
'''
sec_low_mark = sorted(list(set(student_dic.values())))[1];
#another dctionary for storing the second lowest mark student
second_lowest = []
for stud_name, stud_mark in student_dic.items():
    if stud_mark == sec_low_mark:
        second_lowest.append(stud_name)
second_lowest.sort()
for name in second_lowest:
    print(name)
