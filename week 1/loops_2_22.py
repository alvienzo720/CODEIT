
# for loops execute within a given range


# print out all even numbers, excluding 0 using mod
for num in range(100):  
    if num % 2 == 0 and num != 0:
        print(num)

# with a while loop, define a counter variable
count = 0 

# while loops execute when a condition is true, and
# stop when the condition is false

while count < 10:
    count += 1
    print(count)
