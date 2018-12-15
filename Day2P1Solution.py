import sys

#Please pass in the input file "Day2P1Input.txt" as the first input to this .py file on the command line.


def letter_count(id):
	#create an empty dictionary for storing letter counts.
	letter_dict = {}

	#iterate through the string id and count the number of times each letter occurs.
	for letter in id:
		if letter in letter_dict:
			letter_dict[letter]+=1
		else:
			letter_dict[letter] = 1

	#return a list with the first element corresponding to whether or not a letter with a count of exactly 2 occurs and the second element corresponding to whether or not a letter with a count of exactly 3 occurs.
	output_list = [0, 0]

	if 2 in letter_dict.values():
		output_list[0]+=1

	if 3 in letter_dict.values():
		output_list[1]+=1

	return output_list


if __name__ == "__main__":

	#read-input:
	input_ids= open(sys.argv[1], "r")

	#create counters for tracking number of ids that contain any 2 repeat letters and any 3 repeat letters.
	two_counter = 0
	three_counter = 0

	for i in input_ids:
		#run letter_count on the input id
		output_list = letter_count(i)

		#update the counters
		two_counter += output_list[0]
		three_counter += output_list[1]

	#print the "checksum"
	print two_counter * three_counter