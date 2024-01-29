def gather_credits(credit, *args):
    courses = {}
    current_credits = 0

    for index in args:
        if current_credits >= credit:
            break
        if index[0] not in courses:
            courses[index[0]] = index[1]
            current_credits += index[1]

    the_list = [k for k in courses.keys()]
    result = ""

    if current_credits >= credit:
        return f"Enrollment finished! Maximum credits: {current_credits}.\nCourses: {', '.join(sorted(the_list))}"

    return f"You need to enroll in more courses! You have to gather {credit - current_credits} credits more."


print(gather_credits(
    80,
    ("Basics", 27),
))
