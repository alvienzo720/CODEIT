

#Nyeko Samuel

def fib(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        '''
        - this solution only works when variables are initialized on
        the same line because it overwrites a instead of swaping
        using temp
        - initializing the standard way would not work
        in this case since the variables would initalized
        at different times 
        '''
        a, b = b, a+b # intializes a and b at the same time, no need for temp

fib(5)
