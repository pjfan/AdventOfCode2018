# AdventOfCode2018
My solution set (Python) for the Advent of Code 2018 challenges. (Spoilers)

## Approach / Takeaways / Things learned (by problem set):

Day1P1: 
- This one was pretty straight forward so not much really.

Day1P2: 
- In scenarios where you need to keep track of the number of unique elements, the Python built-in set([]) objects are very handy and often more useful than lists. 
- It's faster to have a while loop running with "while True" and have it break as soon as the false condition appears (in this case the first duplicate frequency) than to have it evaluate a statement every iteration that involves the comparison of two large and growing lists. In other words, there's a difference in run-time between running the while loop, catching the first false condition and breaking the while loop and running the while loop, running a comparison between two large list objects, and breaking when the comparison reads False. Calculating and running a comparison between two large lists every iteration is more expensive than simply catching the first false condition.

Day2P1:
- Learned the approximate definition of a checksum.
- Straightforward counting problem. Used a Python dictionary (hash table) for letter counting.

Day2P2:
- Wrote a checker function to compare strings and count # of differences. 
- Compared every element in the list to every other element using a while loop that breaks once the input list is empty and on every iteration pops the end element off the input list and checks it against all remaining elements in the input list.

Day3P1:
- I used a brute-force solution here. I wrote a fabric_square class that calculated the coordinates for the corners of a fabric square and all the coordinates covered by that particular fabric square. I then wrote a check_overlap function that ran an intersection operation on two input fabric_squares objects to see if any of the coordinates in their "space_covered" set matched (overlapped). Since it didn't matter how many times a particular square-inch was overlapped, I used a set object to keep track of all the overlapped spaces since only the number of unique spaces mattered.
- There was a large improvement in run-time speed once I pre-calculated the "space_covered" set of coordinates and stored it as an attribute of the fabric_square object. With 1000+ fabric square inputs and some squares with dimensions nearing 30x30, calculating the complete set of coordinates covered by a single fabric square became an expensive operation when performed every iteration of a loop over every possible unique combination of fabric squares (over 500,000 combos).
- There was a large improvement in run-time once I included a series of 4 preliminary checks in the check_overlap() function that checked to see if the two input squares had any chance of overlapping by comparing the coordinates of their four corners. With a 1000 x 1000 fabric area there is a high probability that many of the squares are nowhere near each other. The preliminary checks allow the check_overlap() function to save time by skipping running a set.intersection() operation on the "space_covered" sets of two squares with no chances of overlapping. 

Day3P2:
- The heuristics described in the previous problem didn't quite work as expected (alot of unexpected edge cases) and I wanted to move on so I just went with the brute-force approach. Brute-force solution was alot quicker here since I didn't have to store/keep track of "spaces_covered".
- Learned that set1.intersection(set2) will not necessarily give me the same answer as set2.intersection(set1).

Day4P1:
- 


