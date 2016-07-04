Height, Width = map(int, input().split())
for i in range(1, Height, 2):
    print((i * ".|.").center(Width, '-'));
print("WELCOME".center(Width, '-'));
for i in range(Height-2, -1, -2):
    print((i*".|.").center(Width, '-'))


# ## from discussions
# n, m = map(int,input().split())
# pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))