nums = tuple([float(x) for x in input().split()])

same_value = {}

for i in range(len(nums)):
    if nums[i] not in same_value.keys():
        same_value[nums[i]] = nums.count(nums[i])

for key, value in same_value.items():
    print(f"{key} - {value} times")
