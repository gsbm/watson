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
__version__ = "1.0.2"

config_file = "config.json"

init(convert=True, autoreset=True)

def load_config(file):
	# load json file
	global sh_dir
	with open(file) as f:
		config = json.load(f)
		f.close()

		sh_dir = config["sherlock_dir"]

def send_requests(file, data, quiet=False):
	# send requests and catch output
	for i in range(0, len(data)):
		if quiet:
			subprocess.call((sh_dir+" "+data[i]), shell=True, stdout=open(os.devnull, 'wb'))

		else:
			subprocess.call((sh_dir+" "+data[i]), shell=True)

		print(Fore.YELLOW+Style.BRIGHT+"[W~:"+Fore.WHITE+file+Fore.YELLOW+"]"+Style.RESET_ALL+" Infos were stored in '"+Style.BRIGHT+data[i]+".txt"+Style.RESET_ALL+"'")

def method(file, csv_format=False, json_format=False, quiet=False):
	# check if the file exist
	if path.exists(file) is True:

		if csv_format:
			# read file
			with open(file, "r") as f:
				data = [line.rstrip() for line in f]
				data = data[0].split(",")

		elif json_format:
			# read file
			with open(file) as json_file :
				data = json.load(json_file)

		else:
			# store each line
			with open(file, "r") as ins:
				data = []
				for fLine in ins:
					data.append(fLine)
					# remove carriage return
					data = [u.rstrip() for u in data]

		print(Fore.YELLOW+Style.BRIGHT+"[W~:"+Fore.WHITE+file+Fore.YELLOW+"]"+Style.RESET_ALL+" {0}".format(len(data))+" username(s) loaded")

		# send requests to sherlock
		send_requests(file, data, quiet)

	else:
		if file != "":
			print(Fore.RED+Style.BRIGHT+"[!]"+Style.RESET_ALL+" There is no such file named '"+Style.BRIGHT+file+Style.RESET_ALL+"'!")

		else:
			print(Fore.RED+Style.BRIGHT+"[!]"+Style.RESET_ALL+" There is no selected file!")


parser = argparse.ArgumentParser(description="Watson: Sherlock assistant to bulk username research", epilog=f"(Version {__version__})")

parser.add_argument("FILE", help="File containing usernames", action='store')
parser.add_argument("-q", "--quiet", dest="quiet", help="Quiet Sherlock progression and keep only essential informations.", action="store_true")
parser.add_argument("--csv", dest="csv", help="Use Comma-Separated Values (CSV) File.", action="store_true")
parser.add_argument("--json", dest="json", help="Use JavaScript Object Notation (JSON) File.", action="store_true")

args = parser.parse_args()

try:
	load_config(config_file)
	method(args.FILE, args.csv, args.json, args.quiet)

except Exception as error:
	print(Fore.RED+Style.BRIGHT+"[!] "+Style.RESET_ALL+str(error))
