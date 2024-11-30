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