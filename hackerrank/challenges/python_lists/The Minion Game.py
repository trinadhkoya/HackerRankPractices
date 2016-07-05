import string
s = input()
l = len(s)

Total = sum([l- i for i in range(l)])
Kscore = sum([l-i if s[i] in 'AEIOU' else 0 for i in range(l)])

if Kscore != Total / 2:
    print('Kevin '  + str(Kscore) if Kscore > Total - Kscore
     else 'Stuart ' + str(Total - Kscore) )
else:
    print('Draw')