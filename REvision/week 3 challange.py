# Week 3 challenge:

# Week 3 challenge:

star = "*"

# for i in range(5):
#     #print(star)
#     star = star+"*" # concatenation

#


# using while loop
# count = 0
# while count < 5:
#     print("Hello" * count)
#     count += 1

alpha = ['a', 'b', 'c']
num = 0
# for i in alpha:
#     #print(i)
#     for m in i:
#         print(i + m)

for i in range(len(alpha)):
    for k in range(len(alpha)):
        print(alpha[i] + alpha[k])

print("-----------------------------")
out_count = 0
in_count = 0
while out_count < 3:
    in_count = 0
    while in_count < 3:
        print(alpha[out_count] + alpha[in_count])
        in_count += 1
    out_count += 1


