clothes = [int(x) for x in input().split()]
rack_space = int(input())

current_rack = rack_space

used_racks = 1

while clothes:
    if current_rack < clothes[-1]:
        current_rack = rack_space - clothes.pop()
        used_racks += 1
    else:
        current_rack -= clothes.pop()

print(used_racks)