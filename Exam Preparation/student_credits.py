def students_credits(*string):
    courses = {}
    diploma = 240
    result = []
    total_score = 0

    for element in string:
        current_element = element.split("-")
        course_name = current_element[0]
        credits = int(current_element[1])
        max_test_points = int(current_element[2])
        diyan_points = int(current_element[3])

        if course_name not in courses:
            courses[course_name] = 0

        total_credits = (diyan_points / max_test_points) * credits
        courses[course_name] = total_credits
        total_score += total_credits

    if total_score >= diploma:
        result.append(f"Diyan gets a diploma with {total_score:.1f} credits.")
    else:
        result.append(f"Diyan needs {diploma - total_score:.1f} credits more for a diploma.")

    for key, value in sorted(courses.items(), key=lambda k: -k[1]):
        result.append(f"{key} - {value:.1f}")

    return "\n".join(result)


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
