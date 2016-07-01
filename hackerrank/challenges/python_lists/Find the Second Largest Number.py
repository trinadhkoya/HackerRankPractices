i = int(input());
mylist = list(map(int, input().split()))[:i];
second_largest = max(mylist);

while max(mylist) == second_largest:
    mylist.remove(max(mylist));
print(max(mylist))
