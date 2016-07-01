a, b, c, d = (int(input()) for _ in range(4));
print([[x, y, z] for x in range(0, a + 1) for y in range(0, b + 1) for z in range(0, c + 1) if x + y + z != d])
