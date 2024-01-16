students = int(input())
grades = {}

for _ in range(students):
    name, score = input().split()
    if name not in grades.keys():
        grades[name] = []

    grades[name].append(float(score))

for key, value in grades.items():
    avg_score = sum(value) / len(value)
    format_value = [f'{x:.2f}' for x in value]

    print(f"{key} -> {' '.join(format_value)} (avg: {avg_score:.2f})")
