dui_chen_year = []

for i in range(2018,3000):
    i_a = str(i)[0]
    i_b = str(i)[1]
    i_c = str(i)[2]
    i_d = str(i)[3]

    thing = int(i_a + i_b + i_c + i_d)

    if i_a == i_d and i_b == i_c:
        dui_chen_year.append(thing)

print(dui_chen_year)