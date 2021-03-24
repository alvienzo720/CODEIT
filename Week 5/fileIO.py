# file Input / Output

#create a file called stock data

import os


def exe1():
    file_path = 'text'

    if not os.path.exists(file_path):
        print("new file created")
        with open(file_path, "w") as f:
            f.write("new file created")
    else:
        print("file exists")
        # a -appends some new text to the existing file
        with open(file_path, "a") as f:
            f.write("here is some text")

#exe1()


def exe2():
    file_path = 'text_example_2'

    if not os.path.exists(file_path):
        f = open(file_path, "w")
        f.write("new file text_example_2 created")
        # rt writes text, overriding existing text frm left to right
    else:
        f= open(file_path, "rt")
        f.write("here is some new text")

    f = open(file_path,"r")
    r = f.read()
    print(r)
    f.close()


exe2()
