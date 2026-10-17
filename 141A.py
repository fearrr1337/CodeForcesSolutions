guest = list(input())
host = list(input())
pile = list(input())


combined = guest + host


combined.sort()
pile.sort()


if combined == pile:
    print("YES")
else:
    print("NO")
