def softuni_students(*args, **kwargs):
    invalid_course = set()
    passed_students = {}

    for id, username in args:
        if id in kwargs:
            course_name = kwargs[id]
            passed_students[username] = course_name
        else:
            invalid_course.add(username)

    result = []

    for key, value in sorted(passed_students.items()):
        result.append(f"*** A student with the username {key} has successfully finished the course {value}!")

    if invalid_course:
        invalid_message = f"!!! Invalid course students: {', '.join(sorted(invalid_course))}"
        result.append(invalid_message)
    return "\n".join(result)


print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
