#!/usr/bin/env python

'''Watson :
Sherlock assistant to bulk username research

Get Sherlock here :
https://github.com/sherlock-project/sherlock
'''

import sys
import os
import os.path
import argparse
import subprocess

from os import path
from colorama import init, Fore, Back, Style

module_name = "Watson"
__version__ = "1.0.0"

# Sherlock directory
sh_dir = 'cd .. && '

init(convert=True, autoreset=True)

def main():
	# Check if the file exist
	if path.exists(myFile) is True:

		if args.csv:
			# Read file
			with open(myFile, "r") as f:
				uArray = [line.rstrip() for line in f]
				uArray2 = uArray[0].split(",")

			# Count items
			fCount = len(uArray2)
			print(Fore.YELLOW+Style.BRIGHT+"[W~:"+Fore.WHITE+myFile+Fore.YELLOW+"]"+Style.RESET_ALL+" {0}".format(fCount)+" username(s) loaded")

			# Send requests to Sherlock
			n = fCount
			for i in range(0, n):
				if args.quiet:
					subprocess.call((sh_dir+"sherlock.py "+uArray2[i]), shell=True, stdout=open(os.devnull, 'wb'))

				else:
					subprocess.call((sh_dir+"sherlock.py "+uArray2[i]), shell=True)

				print(Fore.YELLOW+Style.BRIGHT+"[W~:"+Fore.WHITE+myFile+Fore.YELLOW+"]"+Style.RESET_ALL+" Infos were stored in '"+Style.BRIGHT+uArray2[i]+".txt"+Style.RESET_ALL+"'")

		else:
			# Count lines
			fCount = len(open(myFile).readlines(  ))
			print(Fore.YELLOW+Style.BRIGHT+"[W~:"+Fore.WHITE+myFile+Fore.YELLOW+"]"+Style.RESET_ALL+" {0}".format(fCount)+" username(s) loaded")

			# Store each line
			with open(myFile, "r") as ins:
				uArray = []
				for fLine in ins:
					uArray.append(fLine)
					# Remove carriage return
					uArray2 = [u.rstrip() for u in uArray]

			# Send requests to Sherlock
			n = fCount
			for i in range(0, n):
			#	os.system("sherlock.py "+uArray2[i])
				if args.quiet:
					subprocess.call((sh_dir+"sherlock.py "+uArray2[i]), shell=True, stdout=open(os.devnull, 'wb'))

				else:
					subprocess.call((sh_dir+"sherlock.py "+uArray2[i]), shell=True)

				print(Fore.YELLOW+Style.BRIGHT+"[W~:"+Fore.WHITE+myFile+Fore.YELLOW+"]"+Style.RESET_ALL+" Infos were stored in '"+Style.BRIGHT+uArray2[i]+".txt"+Style.RESET_ALL+"'")

	else:
		if myFile != "":
			print(Fore.RED+Style.BRIGHT+"[!]"+Style.RESET_ALL+" There is no such file named '"+Style.BRIGHT+myFile+Style.RESET_ALL+"' !")

		else:
			print(Fore.RED+Style.BRIGHT+"[!]"+Style.RESET_ALL+" There is no selected file !")

parser = argparse.ArgumentParser(description='Watson : Sherlock assistant to bulk username research', epilog=f'(Version {__version__})')

parser.add_argument('FILE', help="File containing usernames", action='store')
parser.add_argument('-q', '--quiet', dest="quiet", help="Quiet Sherlock progression and keep only essential informations.", action="store_true")
parser.add_argument('--csv', dest="csv", help="Use Comma-Separated Values (CSV) File.", action="store_true")

args = parser.parse_args()

if args.FILE:
	myFile = args.FILE

	try:
		main()

	except:
		print(Fore.RED+Style.BRIGHT+"[!]"+Style.RESET_ALL+" An error occured !")
