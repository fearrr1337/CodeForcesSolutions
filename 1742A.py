t = int(input())

for i in range(t):
    nums = list(map(int, input().split()))
    if nums[1] + nums[2] == nums[0] or nums[0] + nums[1] == nums[2] or nums[0] + nums[2] == nums[1]:
        print("YES")
    else:
        print("NO")