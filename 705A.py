n = int(input())

my_str = ""

for i in range(1, n + 1):
    if i % 2 == 0:
        my_str += "I love"
    else:
        my_str += "I hate"

    if i == n:
        my_str += " it"
    else:
        my_str += " that "

print(my_str)
