long_teng_numbers_int = []

for i in range(1000):
    if i >= 0 and i <= 9:
        i_number = str("000") + str(i)
    elif i >= 10 and i <= 99:
        i_number = str("00") + str(i)
    elif i >= 100 and i <= 999:
        i_number = str("0") + str(i)
    elif i == 1000:
        i_number = str(i)

    i_a = int(i_number[0])
    i_b = int(i_number[1])
    i_c = int(i_number[2])
    i_d = int(i_number[3])

    i_a_str = str(i_number[0])
    i_b_str = str(i_number[1])
    i_c_str = str(i_number[2])
    i_d_str = str(i_number[3])

    append_list_int = int(i_a_str + i_b_str + i_c_str + i_d_str)

    if i_a + i_b + i_c + i_d == 5:
        long_teng_numbers_int.append(append_list_int)


print("int" + str(long_teng_numbers_int))

_j_number = 0

for j in long_teng_numbers_int:
    j_number = long_teng_numbers_int[j]

    if j_number >= 0 and j_number <= 9:
        _j_number = str("000") + str(j_number)
    elif j >= 10 and j <= 99:
        _j_number = str("00") + str(j_number)
    elif j >= 100 and j <= 999:
        _j_number = str("0") + str(j_number)
    elif j == 1000:
        _j_number = str(j_number)


    j_a = 0
    j_b = 0
    j_c = 0
    j_d = 0

    j_a = _j_number[0]
    j_b = _j_number[1]
    j_c = _j_number[2]
    j_d = _j_number[3]