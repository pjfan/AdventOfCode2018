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
		# Some attributes I calculated for heuristics I took out because they led to the wrong answer.
		# self.top_left = self.coordinates
		# self.top_right = [sum(x) for x in zip(self.coordinates, [self.dimensions[0], 0])]
		# self.bot_left = [sum(x) for x in zip(self.coordinates, [0, self.dimensions[1]])] 
		# self.bot_right = [sum(x) for x in zip(self.coordinates, self.dimensions)]
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

#Was going to include the heuristic below but there ended up being too many edge cases (case where a smaller rectangle is completely embedded in a larger one, case where two rectangles overlap in a center patch but not at their corners, etc.) so I removed it. 
#Heuristic: In order for an overlap to occur one of the corners of one square must have an x-coordinate in between the x-coordinates of the corners of the other square and a y-coordiante in between the y-coordinates of the other square.
#Too many edge cases, just brute forced it instead.

#Take two fabric_square instances as input, determine where they overlap by comparing intersection of space_covered set attributes. If they do not overlap then output empty set.
def check_overlap(fab1, fab2):
	return fab1.space_covered.intersection(fab2.space_covered) 



#Please pass in the input file "Day3P1Input.txt" as the first input to this .py file on the command line.
if __name__ == "__main__":

	#read input into a list
	input_ids= open(sys.argv[1], "r")
	input_list = [fabric_square(line.strip()) for line in input_ids]

	#create empty set to keep track of all the positions that are overlapped by two or more squares.
	overlapped_region = set()

	#generate all possible unique combinations of two input squares, iterate over each combinaton and run check_overlap(), update overlapped_region set with results from each check.
	for fab1, fab2 in itertools.combinations(input_list, 2):
		overlapped_region = overlapped_region.union(check_overlap(fab1, fab2))
		print("Checked Overlap: ", fab1.id, fab2.id)

	#The length of the overlapped_region set corresponds to the number of square inches that are overlapped by at least two proposed fabric squares.
	print(len(overlapped_region))


