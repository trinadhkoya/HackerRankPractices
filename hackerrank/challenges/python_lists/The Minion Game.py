import string
s = input()
l = len(s)

Total = sum([l- i for i in range(l)]);
print(Total)
Kscore = sum([l-i if s[i] in 'AEIOU' else 0 for i in range(l)])
print(Kscore)
if Kscore != Total / 2:
    print('Kevin '  + str(Kscore) if Kscore > Total - Kscore
     else 'Stuart ' + str(Total - Kscore) )
else:
    print('Draw')



input_string = str(input());
len_input_string = len(input_string);
total = 0;
# Total = sum([l- i for i in range(l)]);
total = sum(len_input_string - i for i in range(len_input_string))

KEVIN_SCORE=sum( i if input_string[i] in "AEIOU" else 0 for i in range(len_input_string))

if  KEVIN_SCORE!=total/2:
    print('Kevin'+str(KEVIN_SCORE) if KEVIN_SCORE>total-KEVIN_SCORE else 'S')