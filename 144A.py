n = int(input())

my_list = list(map(int, input().split()))

max_index = my_list.index(max(my_list))
min_index = len(my_list) - 1 - my_list[::-1].index(min(my_list))

count = max_index + (n - 1 - min_index)

if max_index > min_index:
    count -= 1

print(count)
