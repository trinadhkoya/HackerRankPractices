N = int(input())
whitespace = len(str(bin(N)).replace('0b', ''))

for i in range(1, N+1):
    bina = bin(int(i)).replace('0b', '').rjust(whitespace, ' ')
    octal = oct(int(i)).replace('0o', '').rjust(whitespace, ' ');
    hexa = hex(int(i)).replace('0x', '').upper().rjust(whitespace, ' ')
    dec = str(i).rjust(whitespace, ' ')
    print (dec, octal, hexa, bina);