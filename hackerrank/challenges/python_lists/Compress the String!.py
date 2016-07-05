from itertools import groupby

parsed_string = str(input());

list = [list(nooftimes) for item, nooftimes in groupby(parsed_string)]
print(list)
for i in list:
    print(tuple((len(i), int(i[0]))), end='')
