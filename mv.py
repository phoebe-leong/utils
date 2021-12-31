#!/usr/bin/env/python3

## An implementation of the "mv" UNIX command ##

import sys
import os
import subprocess

def mv(items, dir):
	if os.path.isdir(dir) == False:
		print("Invalid directory")
		exit(-1)

	mv = "mv"
	if os.name != "posix":
		mv = "move"

	for item in items:
		subprocess.run([mv, item, dir])

def help():
	print("Usage: file.. dir\n")
	print("Multiple files (or directories) can be passed to be moved to a single directory,")
	print("but the directory must be the last argument passed")

	exit(0)

if __name__ == "__main__":
	if len(sys.argv) == 1 or (len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help")):
		help()

	items = []
	i = 1
	while i != len(sys.argv) - 1:
		if os.path.exists(sys.argv[i]) == False:
			print(f"Invalid item: {sys.argv[i]}")
			exit(-1)

		items.append(sys.argv[i])
		i += 1

	mv(items, sys.argv[len(sys.argv) - 1])
	print(f"Successfully moved items into \"{sys.argv[len(sys.argv) - 1]}\"")