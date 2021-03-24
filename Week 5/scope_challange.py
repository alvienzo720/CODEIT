def ex():
    c = "c"
    print(c)
    # defining a nested function

    def mid():
        b = "b"
        print(b)

        def inner():
            global a
            a = "a"

        inner()
        print(a)
    mid()


ex()