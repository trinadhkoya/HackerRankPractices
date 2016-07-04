import textwrap

string = str(input());
givenwidth=int(input());
print(textwrap.fill(string,givenwidth))