mainstring, substring = [str(input()) for _ in range(2)];
counter = 0;
# let us assume line=ALCDCECDCD,target=CDC
for i in range(len(mainstring)):
    '''
     # in iteration 1 --> line[0:0+3] i.e ALC==CDC;
     counter=1
     #in iteration 2-->line[1:1+3] i.e LCD==CDC
    '''
    if mainstring[i:i + len(substring)] == substring:
        counter += 1
print(counter)
