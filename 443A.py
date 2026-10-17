s = input()

cleaned = s.strip("{}").replace(" ", "")

if not cleaned:
    print(0)
else:
    print(len(set(cleaned.split(","))))