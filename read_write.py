def read_content():
    """ read index.html and return content as list """
    content = []
    with open("index.html", "r") as html:
        content = html.readlines()
    
    return content


def find_task_lineindex(content):
    """ find and return the line after which we have task paragraph """
    task_lineindex = 0
    for index, line in enumerate(content):
        if '<div class="taskDescription">' in line:
            task_lineindex = index + 1
            break
    
    return task_lineindex


def read_task():
    """ return the current task paragraph in index.html """
    content = read_content()
    task_index = find_task_lineindex(content)

    return content[task_index]


def update_task(new_text):
    """ update index.html with new task paragraph  """
    content = read_content()
    task_index = find_task_lineindex(content)

    content[task_index] = new_text + "\n"

    with open("index.html", "w") as html:
        html.writelines(content)
