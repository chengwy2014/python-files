num_a = 10000000000
num_b = 101011

sum = str(num_a - num_b)

number_sum_9 = 0

for i in sum:
    # print(i)
    if i == "9":
        number_sum_9 += 1

print(number_sum_9)