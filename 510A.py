n, m = map(int, input().split())

s_div_2 = ("." * (m-1)) + "#"
s_div_1 = "#" * m

for i in range(1, n+1):
    if i % 4 == 0:
        print(s_div_2[::-1])
    elif i % 2 == 0:
        print(s_div_2)
    else:
        print(s_div_1)