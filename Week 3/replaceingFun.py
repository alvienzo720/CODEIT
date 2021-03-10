#
# def replace_func(s, t, n):
#     # string -s, target -t, new -n
#
#     return
#
#
# replace_func()


# string like "hello world"

# target like world

# new word like guys

def replace_func(s, t, n):
    # convert our string to a list as we split it
    s = s.split()
    print(s)
    print(type(s))
    for i in s:  # here we loop through our now list (s)
        if i == t:
            s.pop()
            s.append(n)
            print(' '.join(s))


'''
In this method i managed to replace the last word at the last
index since i was using pop to remove the last word in the list
and i used the joi method to put back the string
'''

replace_func("Hello world", "world", "guys")
