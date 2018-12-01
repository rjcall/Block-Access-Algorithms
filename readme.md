# Assignment 6 - Block Access Algorithms

### Objective:
	In this assignment, you will be writing a program that reads a list of disk block access requests from stdin or from a file specified on the command line.
	That list will be used four times to run through the following block access algorithms:
	
		1. First Come, First Served
		2. Shortest Seek Time First
		3. Non-circular LOOK
		4. Circular LOOK

	Your program will show the total seek values for each algorithm. 
	The first value from the list is the most recent completed block request, and thus is the current block position for the device. 
	Your program only needs to work with a maximum of 100 block requests. 
	For the LOOK and C-LOOK algorithms, you start seeking in the positive direction.


### Usage: 
	
	Works with either Python2 or Python3.
	
	Directions:
		1. Open terminal in assn6 folder
		2. ../assn6/# python assn6.py <FILENAME.txt>


### Output: With this block-list.txt

	# python assn6.py block-list.txt

	Assignment 6: Block Access Algorithm
	By: Robert Call

	FCFS Total Seek: 1594
	SSTF Total Seek: 287
	LOOK Total Seek: 269
	C-LOOK Total Seek: 477