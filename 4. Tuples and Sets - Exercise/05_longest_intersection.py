lines = int(input())
longest_intersection = set()

for i in range(lines):
    action = input().split("-")

    first_split = [int(x) for x in action[0].split(",")]
    second_split = [int(x) for x in action[1].split(",")]

    range_one = set([i for i in range(first_split[0], first_split[1] + 1)])
    range_two = set([j for j in range(second_split[0], second_split[1] + 1)])
    current_intersection = range_one.intersection(range_two)

    if len(current_intersection) > len(longest_intersection):
        longest_intersection = current_intersection

formated_intersection = [num for num in longest_intersection]

print(f"Longest intersection is {formated_intersection} with length {len(formated_intersection)}")
