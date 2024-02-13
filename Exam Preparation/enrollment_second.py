def gather_credits(credits_target, *args):
    result = []

    courses = []
    credits = 0

    for current_course, course_credits in args:
        if credits >= credits_target:
            break
        if current_course in courses:
            continue

        courses.append(current_course)
        credits += course_credits

    if credits >= credits_target:
        result.append(f"Enrollment finished! Maximum credits: {credits}.")
        result.append(f"Courses: {', '.join(sorted(courses))}")
    else:
        result.append(
            f"You need to enroll in more courses! You have to gather {credits_target - credits} credits more.")

    return "\n".join(result)


print(gather_credits(
    80,
    ("Basics", 27),
))
