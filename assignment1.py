import math
def sum_of_sqr_dif(data_set, avg):
  	result = 0
	for i in data_set:
		result += (i - avg) * (i - avg)
  	return result

def compute_median(data_set):
	result = 0
	if (len(data_set) % 2 == 0):
		result = 0.5 * (data_set[len(data_set)/2] + data_set[(len(data_set)/2) - 1])
	else:
		result = data_set[(len(data_set) / 2)]
	return result
# Problem 1.17

smokers = [13.8, 22.1, 23.2, 34.4, 43.8, 47.6, 48.1, 52.7, 53.2, 56.0, 60.2, 69.3]
nonsmokers = [28.6,25.1, 26.4, 29.8, 28.4, 38.5, 30.6, 31.8, 41.6, 36.0, 37.9, 13.9,
 			  34.9,30.2, 21.1]

smokers_avg = sum(smokers) / 12.0
sum_of_square_difference = sum_of_sqr_dif(smokers, smokers_avg)
sqrt_quotient_smokers = math.sqrt(sum_of_square_difference / 11)

print "Smokers' average is: %f" %smokers_avg
print "Smokers' sd is: %f" %(sqrt_quotient_smokers)

nonsmokers_avg = sum(nonsmokers) / 15.0
sum_of_square_difference = sum_of_sqr_dif(nonsmokers, nonsmokers_avg)
sqrt_quotient_nonsmokers = math.sqrt(sum_of_square_difference / 14)

print "Nonsmokers' average is: %f" %nonsmokers_avg
print "Nonsmokers' sd is: %f" %(sqrt_quotient_nonsmokers)

# Problem 1.19
fuel_pumps = [2.0, 3.0, 0.3, 3.3, 1.3, 0.4, 0.2, 6.0, 5.5, 6.5, 0.2, 2.3,
			  1.5, 4.0, 5.9, 1.8, 4.7, 0.7, 4.5, 0.3, 1.5, 0.5, 2.5, 5.0,
			  1.0, 6.0, 5.6, 6.0, 1.2, 0.2]

fuel_pumps_avg = sum(fuel_pumps)/30
sum_of_square_difference = sum_of_sqr_dif(fuel_pumps, fuel_pumps_avg)
sqrt_quotient_fuel_pumps = math.sqrt(sum_of_square_difference / 29)

print "Fuel pump average is: %f" %fuel_pumps_avg
print "Fuel pump sd is: %f" %sqrt_quotient_fuel_pumps

# Problem 1.20

length_of_life = [17, 20, 10, 9, 23, 13, 12, 19, 18, 24, 12, 14, 6, 9, 13, 6, 7,
				  10, 13, 7, 16, 18, 8, 13, 3, 32, 9, 7, 10, 11, 13, 7, 18, 7,
				  10, 4, 27, 19, 16, 8, 7, 10, 5, 14, 15, 10, 9, 6, 7, 15]
length_of_life.sort()
interval = [10, 20, 30, 40]
frequency = [0.0, 0.0, 0.0, 0.0]
i = j = 0

while (i < 4 and j < 50):
	if length_of_life[j] >= interval[i]:
		i = i + 1
	frequency[i] = frequency[i] + 1
	j = j + 1

i = 0
while (i < 4):
	print "interval %d to %d has a frequency %d with relative frequency %f"%(interval[i] - 10,
	interval[i], frequency[i], frequency[i]/len(length_of_life))
	i = i + 1

print compute_median(length_of_life)
print sorted(length_of_life)
