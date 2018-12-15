import sys

#Please pass in the input file "Day1P1Input.txt" as the first input to this .py file on the command line.

if __name__ == "__main__":

	#read-input:
	input_num = open(sys.argv[1], "r")

	#read inputs into a list
	input_list = [int(x) for x in input_num]

	#set variables
	frequency_set = set([0])
	current_frequency = 0

	counter = 0
	input_len = len(input_list)

	#repeat this while loop until a frequency is repeated
	while True:
		#increment current_frequency
		current_frequency += input_list[counter]

		#save new frequency to set if it hasn't been seen before, else print the repeat frequency and break.
		if current_frequency not in frequency_set:
			frequency_set.add(current_frequency)
		else: 
			print(current_frequency)
			break

		#increment counter, reset to 0 if it's reached end of input list
		counter+=1
		if counter == input_len:
			print("At: ", current_frequency)
			counter = 0