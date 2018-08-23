#!/usr/bin/python
"""A parser of /var/log/puppet.log.

Imports argparse for parsing arguments and then the script
accepts file path and year as optional argument. 
"""


import argparse 
from datetime import datetime
import dateutil.parser
import re
import collections
import os


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument(help="parse the given filename", type=str, dest="filename", action="store")
	parser.add_argument("-y","--year", help="parse file with given year", type=int, dest="year", action="store")
	args = parser.parse_args()
	if args.year:
		print("year to use: " + str(args.year))
		year = args.year

	else:
		year = datetime.utcfromtimestamp(os.stat(args.filename).st_mtime).year
	
	puppet_parser(args.filename,year)


def puppet_parser(filepath, year):
	"""Accepts the puppet file path and parses it out by calling other functions.

	"""
	#TODO use year from last modification

	# pattern to match from log file and group each finding for referencing
	# pattern looks for a time foormat (x:x:x)any text after which is
	# followed by the process and so on 
	pattern = re.compile(r'(^.+:..:..)\s(\S+)\s(\S+)(\[\d+\]):\s(.+$)')
	#group 1 = date
	#group 2 = hostname
	#group 3 = proccess
	#group 4 = PID
	#group 5 = message
	
	# add to list for counter purposes 
	message_list = []
	proccess_list =[]
	hostname_list= []
	processID_list = []
	
	
	f = open(filepath, "rU")
	for line in f:

		if pattern.match(line):
			if dateutil.parser.parse(pattern.match(line).group(1)).date().year == year:
				
				hostname_list.append(pattern.match(line).group(2))
				proccess_list.append(pattern.match(line).group(3))
				processID_list.append(pattern.match(line).group(4))
				message_list.append(pattern.match(line).group(5))
				

	f.close()

	uniq_process(proccess_list)
	hostnames(hostname_list)
	top_messages(message_list)
	
	

def parse_log(logDictionary):
	"""Prints dictionary in order

	"""
	#get dictionary and paste it in order 
	for x in logDictionary:
		print x


def print_log(dic):
	"""Print entire log.

	"""
	for k, v in sorted(dic.items()):
		print "%s %s %s %s %s" % (k, v[0], v[1], v[2], v[3])


def uniq_process(proccessList):
	"""Unique processes sorted by appearance.

	"""

	proc_sorted = collections.Counter(proccessList).most_common()
	print("Unique Proccess(sorted): ")
	for each in proc_sorted:
		print("["+str(each[1])+"]" +" " + each[0])


def top_messages(messageList):
	"""List top 10 messages in the file.

	"""

	messages = collections.Counter(messageList).most_common(10)
	print("Top 10 Messages: ")
	for each in messages:
		print(each[0])


def hostnames(hostnameList):
	"""Prints hostnames from list.

	"""
	
	hosts = collections.Counter(hostnameList)
	print("Hostsnames in file: ")
	for each in hosts:
		print(each)


if __name__ == '__main__':
	main()