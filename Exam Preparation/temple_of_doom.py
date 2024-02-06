from collections import deque

tools = deque([int(element) for element in input().split()])
substances = [int(element) for element in input().split()]
challenges = [int(element) for element in input().split()]

while True:
    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break
    if not tools or not substances:
        print("Harry is lost in the temple. Oblivion awaits him.")
        break
    current_tool = tools.popleft()
    current_substance = substances.pop()

    temp_total = current_tool * current_substance

    if temp_total in challenges:
        challenges.remove(temp_total)
    else:
        current_tool += 1
        tools.append(current_tool)
        current_substance -= 1
        if current_substance != 0:
            substances.append(current_substance)

if tools:
    tools_conversion = [str(tools[element]) for element in range(len(tools))]
    print(f"Tools: {', '.join(tools_conversion)}")
if substances:
    substance_conversion = [str(substances[element]) for element in range(len(substances))]
    print(f"Substances: {', '.join(substance_conversion)}")
if challenges:
    challenges_conversion = [str(challenges[element]) for element in range(len(challenges))]
    print(f"Challenges: {', '.join(challenges_conversion)}")
