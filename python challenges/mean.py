mean1 = 38
wrong_number = 36
correct_number = 56
total_numbers = 40

initial_sum = mean1 * total_numbers
print("Total sum of 40 numbers:", initial_sum)

correct_sum = initial_sum - wrong_number + correct_number
print("Corrected sum:", correct_sum)

corrected_mean = correct_sum / total_numbers
print("Corrected mean:", corrected_mean)