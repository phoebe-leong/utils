#!/usr/bin/env/python3

## An implementation of the "yes" UNIX command ##

import sys
import time

def pipe_help():
	print("When piping to another program, you must know the exact amount of times that input is needed and forward that to the program.\n")
	print(f"This can be achieved using the following usage: python3 {sys.argv[0]} -1 1")
	print("As you can see, the sleep input is ignored and the program is told to only print out \"yes\" once.")
	print("If -1 is passed to any of the last two arguments then it is ignored. This can be used to skip over sleep, thus producing a working pipe command.")

	exit(0)

# Print the first argument "amt" amount of times, or infinitely if no valid value is passed to "amt".
# After each iteration, if "sleep" is not equal to -1, wait "sleep" seconds until continuing.
def yes(string, sleep, amt):
	if (amt != -1):
		for i in range(amt):
			print(string)

			if sleep != -1:
				time.sleep(sleep)
	else:
		try:
			while True:
				print(string)

				if sleep != -1:
					time.sleep(sleep)
		except KeyboardInterrupt:
			exit(0)

def help():
	print(f"Usage: python3 {sys.argv[0]} string sleep amt")
	print("\tThe \"sleep\" argument refers to how long you want the program to wait before continuing after each iteration,")
	print("\tand the \"amt\" argument refers to the amount of times you want the string to print\n")

	print("\tThe last two arguments are optional")
	print("\t--pipe or -p can be passed to gain help with piping to another program")
	exit(0)


if __name__ == "__main__":
	try:
		# Mimics original "yes" command, defaulting to "yes" infinitely if no arguments are provided
		if len(sys.argv) == 1:
			yes("yes", -1, -1)
		elif len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
			help()
		elif len(sys.argv) == 2 and (sys.argv[1] == "-p" or sys.argv[1] == "--pipe"):
			pipe_help()
		else:
			try:

				if len(sys.argv) == 4:
					yes(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
				elif len(sys.argv) == 3:
					yes(sys.argv[1], int(sys.argv[2]), -1)
				elif len(sys.argv) == 2:
					yes(sys.argv[1], -1, -1)
				else:
					help()
			except ValueError:
				print("Invalid last argument/s")
	except BrokenPipeError:
		pipe_help()