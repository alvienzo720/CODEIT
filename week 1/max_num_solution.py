
#Solution

def max_num():
    l = [1, 5, 3, 2, 4, 334, 52]
    max = 0
    for i in range(len(l)):
        if max < l[i]:
            max = l[i]
    
    print(max)

max_num()

# Collins solution

l = [1, 5, 3, 2, 4, 334, 52]

l = sorted(l)

print(l[-1])
