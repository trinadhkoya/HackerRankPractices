N = int(input());
emp_list = [];
for _ in range(N):
    passed_string = input().split();
    if (passed_string[0] == "insert"):
        emp_list.insert(int(passed_string[1]), int(passed_string[2]));
    elif (passed_string[0] == "remove"):
        emp_list.remove(int(passed_string[1]));
    elif (passed_string[0] == "append"):
        emp_list.append(int(passed_string[1]))
    elif (passed_string[0] == "sort"):
        emp_list.sort();
    elif (passed_string[0] == "pop"):
        emp_list.pop();
    elif (passed_string[0] == "reverse"):
        emp_list.reverse()
    else:
        print(emp_list)
