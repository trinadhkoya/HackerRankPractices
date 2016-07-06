N = int(input());
mylist = list(map(int, input().split()))[:N];
myset = set(mylist);
print(myset,len(myset));
print(sum(myset)/len(myset))
