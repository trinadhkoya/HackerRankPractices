M = int(input());
m_space_sep_integers = input().split();
N = int(input());
n_space_sep_integers = input().split();
setA = (set(map(int, m_space_sep_integers)));
setB = (set(map(int, n_space_sep_integers)));

lis_items = [x for x in setA.difference(setB)]
lis_items.extend([x for x in setB.difference(setA)]);
lis_items.sort();
for x in lis_items:
    print(x)
    # m = int(input())
    # ls = [int(x) for x in input().split()]
    # s1 = set(ls)
    #
    # n = int(input())
    # ls = [int(x) for x in input().split()]
    # s2 = set(ls)
    #
    # print(*s1 ^ s2,end="\n");
    #
    #
    # ls = [x for x in s1.difference(s2)]
    # ls.extend([x for x in s2.difference(s1)])
    # ls.sort()
    #
    # for x in ls:
    #     print(x)
