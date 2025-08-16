FILEPATH = "todos.txt"

def get_todos(filename=FILEPATH):
    """

    :param filename: filename of todos file
    :return: list of todos

    Read the todos file and return a list of todos.
    """
    with open(filename, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_local, filename=FILEPATH):
    """
    :param todos_local: list of modified todos
    :param filename: filename of todos file to write modified todos
    :return: None

    Write the modified todos to a file.
    """
    with open(filename, "w") as file_local:
        file_local.writelines(todos_local)


def greet(hour_of_day):
    """
    :param hour_of_day: hour of day as str or int
    :return: greeting message

    Takes hour of day and returns greeting message.
    """
    hour_of_day = int(hour_of_day)
    if hour_of_day < 12:
        return "Good morning"
    elif hour_of_day < 18:
        return "Good afternoon"
    else:
        return "Good evening"


def append_todo(todo, filename=FILEPATH):
    """
    :param todo: todo to append to file
    :param filename: file to append to
    :return: None

    Takes todo and filename="todos.txt" and appends todo at the end of file.
    """
    with open(filename, "a") as file:
        file.write(f"{todo}\n")
