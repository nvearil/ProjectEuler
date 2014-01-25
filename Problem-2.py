# 0,1,1,2,3,5,8,13,21,34,55

maximum_term = int(raw_input("Maximum term?:"))
current_term_value = 1
previous_term_value = 0
sum_of_even_terms = 2

while (current_term_value + previous_term_value) < maximum_term:
	if (current_term_value + previous_term_value) == 1:
		previous_term_value = 1
		
	elif (current_term_value + previous_term_value) == 2:
		current_term_value = 2
		
	else:
		term_holder = current_term_value
		current_term_value += previous_term_value
		previous_term_value = term_holder
		if current_term_value > 2 and current_term_value % 2 == 0:
			sum_of_even_terms += current_term_value
		
print(sum_of_even_terms)