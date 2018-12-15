import sys

#Please pass in the input file "Day1P1Input.txt" as the first input to this .py file on the command line.

if __name__ == "__main__":

	#read-input:
	input_num = open(sys.argv[1], "r")

	#set counter
	sum_of_input = 0
	frequencies = []

	#loop over inputs and sum results
	for line in input_num:
		sum_of_input += int(line)	

	#view result
	print(sum_of_input)