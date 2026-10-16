n = int(input())

little_x = list(map(int, input().split()))
little_y = list(map(int, input().split()))

levels_x = little_x[1:]
levels_y = little_y[1:]

set_xy = set(levels_x + levels_y)

if len(set_xy) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")