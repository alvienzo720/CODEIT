
moutains = [['Ngaliema', 16762], ['Elgon', 14177], ['Speke', 16043],
 ['Muhavura', 13540], ['Gessi', 15469], ['Moroto', 10115], ['Kadam', 10049]
            ]
# print(moutains)
#
# print(len(moutains))
#
# print(moutains[5])
#
# print(moutains[5][1])

name_list = [['Jay', 15], ['Elijah', 20]]

e = name_list[0][1]

print(e)

# challlanege

# convert Mt . Gessi's height in ft to meters

mt_gessi = moutains[4][1]

mt_gessi_in_meters = mt_gessi / 3.381

# print(mt_gessi_in_meters)


def to_meters():
    for i in moutains:
        print(f"{i[0]}  {round(i[1] / 3.281)}")



to_meters()


name_list = [['Ivan', 15], ['Ahabyona', 70]]

print(len(name_list))  # what will this print out?