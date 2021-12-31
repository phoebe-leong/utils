#!/usr/bin/env/python3

## Find all instances of text in a file - supports wildcard syntax ##

import sys

def find(filename, string):
	try:
		file = open(filename)
	except FileNotFoundError:
		print("Invalid file")
		exit(-1)

	line_num = 1
	for line in file:
		for i in range(len(line)):

			# Iterate through the line and compare the characters to string's characters
			if line[i] == string[0]:
				str_index = 1
				line_index = i + 1

				while str_index != len(string) and line_index != len(line):
					if line[line_index] != string[str_index]:
						break

					str_index += 1
					line_index += 1

				if str_index == len(string):
					print(f"\"{string}\" found on line {line_num}:")
					print(f"{line}")
		line_num += 1
	file.close()

def front_find(filename, string):
	try:
		file = open(filename)
	except FileNotFoundError:
		print("Invalid file")
		exit(-1)

	line_num = 1
	for line in file:
		for i in range(len(line)):

			# Checking that there aren't any other characters in front of the string found
			if line[i] == string[0] and (i == 0 or line[i - 1] == ' '):
				str_index = 1
				line_index = i + 1

				while str_index != len(string) and line_index != len(line):
					if line[line_index] != string[str_index]:
						break

					str_index += 1
					line_index += 1

				if str_index == len(string):
					print(f"\"{string}\" found on line {line_num}:")
					print(f"{line}")
		line_num += 1
	file.close()

def back_find(filename, string):
	try:
		file = open(filename)
	except FileNotFoundError:
		print("Invalid file")
		exit(-1)

	line_num = 1
	for line in file:
		for i in range(len(line)):
			if line[i] == string[0]:
				str_index = 1
				line_index = i + 1

				while str_index != len(string) and line_index != len(line):
					if line[line_index] != string[str_index]:
						break

					str_index += 1
					line_index += 1

				if str_index == len(string):

					# Checking the end of the string for either a termination character or whitespace
					if line_index == len(line) or (line_index != len(line) and (line[line_index] == ' ' or line[line_index] == '\n')):
						print(f"\"{string}\" found on line {line_num}:")
						print(f"{line}")
		line_num += 1
	file.close()

#--#######################################################################################################################################--#

def help():
	print(f"Usage: python3 {sys.argv[0]} filename string")
	exit(0)

if __name__ == "__main__":
	if len(sys.argv) == 1 or (len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help")):
		help()

	string = sys.argv[2]
	stripped_str = ""

	# Really, wildcard syntax is easy
	if string[0] == '%' and string[len(string) - 1] != '%':

		# Strip string of it's %
		i = 1
		while i != len(string):
			stripped_str += string[i]
			i += 1

		front_find(sys.argv[1], stripped_str)
	elif string[0] != '%' and string[len(string) - 1] == '%':
		for i in range(len(string) - 1):
			stripped_str += string[i]

		back_find(sys.argv[1], stripped_str)
	else:
		if string[0] == '%':
			i = 1

			while i != len(string) - 1:
				stripped_str += string[i]
				i += 1
		else:
			stripped_str = string

		find(sys.argv[1], stripped_str)