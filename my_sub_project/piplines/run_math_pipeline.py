from my_sub_project.calculations import math_funcs


def collect():
    task = math_funcs.add.delay(1, 2)
    print(task.get())


if __name__ == '__main__':
    collect()
