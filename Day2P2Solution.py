import sys

def match_ids(id1, id2):
	#track the number of differences between the two id strings and the index at which the difference occurs.
	differences = 0
	index_of_differences = []
	#iterate over the first string and compare it character by character with the second string.
	for i, x in enumerate(id1):
		if x == id2[i]:
			continue
		else:
			differences+=1
			index_of_differences.append(i)
			if differences > 1:
				return False
	#If the for loop completes without finding two differences, print the two strings, the common letters in between the two, and return True.
	print("ID1: ", id1)
	print("ID2: ", id2)

	#If there's a single difference then print the string (either id1 or id2) with the single difference removed. Else just print id1 if strings are the same.
	if differences > 0:
		print("Common letters: ", id1[:index_of_differences[0]] + id1[index_of_differences[0]+1:])
	else:
		print("Common letters: ", id1)
	
	return True

#Please pass in the input file "Day2P1Input.txt" as the first input to this .py file on the command line.
if __name__ == "__main__":

	#read input into a list
	input_ids= open(sys.argv[1], "r")
	input_list = [x for x in input_ids]

	#iterate through input list, pop an element off end of list each iteration and compare it to all the other id's using a for loop + match_ids() until a match is found or all elements are popped off the list.
	while len(input_list) > 0:
		current_id = input_list.pop()
		for i in input_list:
			if match_ids(i.strip(), current_id.strip()):
				input_list = []
				break
			else: 
				continue
		