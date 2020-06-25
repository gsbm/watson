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
import json

from os import path
from colorama import init, Fore, Back, Style

module_name = "Watson"
__version__ = "1.0.0"

debug = False

# Sherlock directory
sh_dir = 'cd .. && '

init(convert=True, autoreset=True)

def main():
	# Check if the file exist
	if path.exists(myFile) is True:

		if args.csv:
			# Read file
			with open(myFile, "r") as f:
				data = [line.rstrip() for line in f]
				data = data[0].split(",")

			# Count items
			itemCount = len(data)
			print(Fore.YELLOW+Style.BRIGHT+"[W~:"+Fore.WHITE+myFile+Fore.YELLOW+"]"+Style.RESET_ALL+" {0}".format(itemCount)+" username(s) loaded")

			# Send requests to Sherlock
			n = itemCount
			for i in range(0, n):
				if args.quiet:
					subprocess.call((sh_dir+"sherlock.py "+data[i]), shell=True, stdout=open(os.devnull, 'wb'))

				else:
					subprocess.call((sh_dir+"sherlock.py "+data[i]), shell=True)

				print(Fore.YELLOW+Style.BRIGHT+"[W~:"+Fore.WHITE+myFile+Fore.YELLOW+"]"+Style.RESET_ALL+" Infos were stored in '"+Style.BRIGHT+data[i]+".txt"+Style.RESET_ALL+"'")

		elif args.json:
			# Check if selected file is a JSON file
			if not myFile.endswith('.json'):
				print(Fore.RED+Style.BRIGHT+"[!]"+Style.RESET_ALL+" The selected file is not a JSON file.")

			else:
				# Read file
				with open(myFile) as json_file :
					data = json.load(json_file)

				# Count items
				itemCount = len(data)
				print(Fore.YELLOW+Style.BRIGHT+"[W~:"+Fore.WHITE+myFile+Fore.YELLOW+"]"+Style.RESET_ALL+" {0}".format(itemCount)+" username(s) loaded")

				# Send requests to Sherlock
				n = itemCount
				for i in range(0, n):
					if args.quiet:
						subprocess.call((sh_dir+"sherlock.py "+data[i]), shell=True, stdout=open(os.devnull, 'wb'))

					else:
						subprocess.call((sh_dir+"sherlock.py "+data[i]), shell=True)

					print(Fore.YELLOW+Style.BRIGHT+"[W~:"+Fore.WHITE+myFile+Fore.YELLOW+"]"+Style.RESET_ALL+" Infos were stored in '"+Style.BRIGHT+data[i]+".txt"+Style.RESET_ALL+"'")

		else:
			# Count lines
			itemCount = len(open(myFile).readlines(  ))
			print(Fore.YELLOW+Style.BRIGHT+"[W~:"+Fore.WHITE+myFile+Fore.YELLOW+"]"+Style.RESET_ALL+" {0}".format(itemCount)+" username(s) loaded")

			# Store each line
			with open(myFile, "r") as ins:
				data = []
				for fLine in ins:
					data.append(fLine)
					# Remove carriage return
					data = [u.rstrip() for u in data]

			# Send requests to Sherlock
			n = itemCount
			for i in range(0, n):
			#	os.system("sherlock.py "+data[i])
				if args.quiet:
					subprocess.call((sh_dir+"sherlock.py "+data[i]), shell=True, stdout=open(os.devnull, 'wb'))

				else:
					subprocess.call((sh_dir+"sherlock.py "+data[i]), shell=True)

				print(Fore.YELLOW+Style.BRIGHT+"[W~:"+Fore.WHITE+myFile+Fore.YELLOW+"]"+Style.RESET_ALL+" Infos were stored in '"+Style.BRIGHT+data[i]+".txt"+Style.RESET_ALL+"'")

	else:
		if myFile != "":
			print(Fore.RED+Style.BRIGHT+"[!]"+Style.RESET_ALL+" There is no such file named '"+Style.BRIGHT+myFile+Style.RESET_ALL+"' !")

		else:
			print(Fore.RED+Style.BRIGHT+"[!]"+Style.RESET_ALL+" There is no selected file !")

parser = argparse.ArgumentParser(description='Watson : Sherlock assistant to bulk username research', epilog=f'(Version {__version__})')

parser.add_argument('FILE', help="File containing usernames", action='store')
parser.add_argument('-q', '--quiet', dest="quiet", help="Quiet Sherlock progression and keep only essential informations.", action="store_true")
parser.add_argument('--csv', dest="csv", help="Use Comma-Separated Values (CSV) File.", action="store_true")
parser.add_argument('--json', dest="json", help="Use JavaScript Object Notation (JSON) File.", action="store_true")

args = parser.parse_args()

if args.FILE:
	myFile = args.FILE

	if debug:
		main()

	else:
		try:
			main()

		except Exception as error:
			print(Fore.RED+Style.BRIGHT+"[!]"+Style.RESET_ALL+" Error : "+str(error))
