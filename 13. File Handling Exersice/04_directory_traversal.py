import os


def check_extension(dir_level, first_level=False):
    for file in os.listdir(dir_level):
        path_file = os.path.join(dir_level, file)

        if os.path.isfile(path_file):
            extens = file.split(".")[-1]
            my_ext[extens] = my_ext.get(extens, []) + [file]
        elif os.path.isdir(file) and not first_level:
            check_extension(path_file, first_level=True)


dir_to_check = input()
my_ext = {}
result = []

check_extension(dir_to_check)
the_report = open("resources/report.txt", "w")

for key, value in sorted(my_ext.items(), key=lambda k: k[0]):

    the_report.write(f".{key}\n")
    for index in value:
        the_report.write(f"- - - {index}\n")

the_report.close()
