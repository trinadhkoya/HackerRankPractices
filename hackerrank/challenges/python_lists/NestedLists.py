#empty dictionary
d = {}
#looping till the given int satisfied
for _ in range(int(input())):  # 2
    Name = input()  # 3
    Grade = float(input())  # 4
    #d['name']=5.0
    d[Name] = Grade  # 5
#listing out values in dictionary
v = d.values()  # 6
#eleminating dupliactaes and make it listed .with sorting any way we could
second = sorted(list(set(v)))[1]
second_lowest = []  # 8
for key, value in d.items():
    if value == second:
        second_lowest.append(key)
second_lowest.sort()  # 12
for name in second_lowest:
    print(name)
