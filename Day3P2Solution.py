import sys
import itertools

#Definining this coordinate system used as:
#x-coordinate = inches to the right from the origin (top left corner)
#y-coordinate = inches in the downwards direction from the origin (top left corner)

class fabric_square:
	def __init__(self, fabric_str):
		fabric_info = self.read_fabric_info_str(fabric_str)
		self.id = fabric_info[0]
		self.coordinates = fabric_info[1]
		self.dimensions = fabric_info[2]
		self.x_max_range = self.coordinates[0] + self.dimensions[0]
		self.y_max_range = self.coordinates[1] + self.dimensions[1]
		self.space_covered = set(self.space_covered())

	def read_fabric_info_str(self, fabric_str):
		#Split the info string on spaces.
		fabric_info_list = fabric_str.split(" ")

		#parse out the fabric id
		fabric_id = int(fabric_info_list[0].strip("#"))

		#parse out the coordinates and dimensions
		fabric_coordinates = fabric_info_list[2].strip(":").split(",")
		fabric_dimensions = fabric_info_list[3].split("x")

		#convert coordinates and dimensions into ints
		fabric_coordinates = [int(x) for x in fabric_coordinates]
		fabric_dimensions = [int(x) for x in fabric_dimensions]

		return [fabric_id, fabric_coordinates, fabric_dimensions]

	def space_covered(self):
		#Generate a list of tuples representing all coordinates covered by this square.
		space_covered = list(itertools.product(range(self.coordinates[0], self.x_max_range), range(self.coordinates[1], self.y_max_range)))
		return space_covered

#Brute force check_overlap by comparing the number of spaces in common between two spaces_covered sets.
def check_overlap(fab1, fab2):
	return fab1.space_covered.intersection(fab2.space_covered)


#Please pass in the input file "Day3P1Input.txt" as the first input to this .py file on the command line.
if __name__ == "__main__":

	#read input into a list
	input_ids= open(sys.argv[1], "r")
	input_list = [fabric_square(line.strip()) for line in input_ids]

	#create empty set to keep track of all the positions that are overlapped by two or more squares.
	overlap_set = set()

	#generate all possible unique combinations of two input squares, iterate over each combinaton and run check_overlap(), update overlapped_region set with results from each check.
	for fab1, fab2 in itertools.combinations(input_list, 2):
		print("Checked Overlap: ", fab1.id, fab2.id)
		overlap_pts = check_overlap(fab1, fab2)
		#If there is an overlap (if check_overlap does not return an empty set object) then add both fabric square ids to the overlap_set set object.
		if overlap_pts != set():
			print("Overlap detected: ", fab1.id, fab2.id)
			overlap_set.add(fab1.id)
			overlap_set.add(fab2.id)
		else:
			print("No Overlap: ", fab1.id, fab2.id)

	#print out the id for the single fabric_square that is in the input_list set but not in the overlap_set.
	print(set([x.id for x in input_list]).difference(overlap_set))


