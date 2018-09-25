#!/usr/bin/python
"""A parser of /var/log/puppet.log.

<<<<<<< HEAD

=======
Imports argparse for parsing arguments and then the script
accepts file path and year as optional argument. 
>>>>>>> ac2c15e85a07012ffbe7491bf511d6ceb3cee872
"""


import argparse 
from datetime import datetime
import dateutil.parser
import re
import collections
import os


def main():
	parser = argparse.ArgumentParser()
<<<<<<< HEAD
	parser.add_argument(
		help="parse the given filename", type=str, 
		dest="filename", action="store")
	parser.add_argument(
		"-y","--year", help="parse file by setting start year", 
		type=int, dest="year", action="store")
	args = parser.parse_args()
	if args.year:
		print("year to use: {0:d}".format(args.year))
		year = args.year

	else: #build year for date parsing
		year = datetime.utcfromtimestamp(
			os.stat(args.filename).st_birthtime).year
		# print("creation of file: {0:d}".format(year))

=======
	parser.add_argument(help="parse the given filename", type=str, dest="filename", action="store")
	parser.add_argument("-y","--year", help="parse file with given year", type=int, dest="year", action="store")
	args = parser.parse_args()
	if args.year:
		print("year to use: " + str(args.year))
		year = args.year

	else:
		year = datetime.utcfromtimestamp(os.stat(args.filename).st_mtime).year
	
>>>>>>> ac2c15e85a07012ffbe7491bf511d6ceb3cee872
	puppet_parser(args.filename,year)


def puppet_parser(filepath, year):
	"""Accepts the puppet file path and parses it out by calling other functions.

	"""
<<<<<<< HEAD
=======
	#TODO use year from last modification
>>>>>>> ac2c15e85a07012ffbe7491bf511d6ceb3cee872

	# pattern to match from log file and group each finding for referencing
	# pattern looks for a time foormat (x:x:x)any text after which is
	# followed by the process and so on 
<<<<<<< HEAD
	pattern = re.compile(
		r'(^.+:..:..)\s(\S+)\s(\S+)(\[\d+\]):\s(.+$)')
=======
	pattern = re.compile(r'(^.+:..:..)\s(\S+)\s(\S+)(\[\d+\]):\s(.+$)')
>>>>>>> ac2c15e85a07012ffbe7491bf511d6ceb3cee872
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
	
<<<<<<< HEAD
	looped = 0
	with open(filepath, "rU") as f:
		for line in f:
			if not pattern.match(line):
				continue
 
			current_date = pattern.match(line).group(1)
			if looped >= 1:
				if (dateutil.parser.parse(prv_date).month <
					dateutil.parser.parse(current_date).month):
					year+=1
			
			set_date = (current_date + " " + str(year))
			hostname_list.append(pattern.match(line).group(2))
			proccess_list.append(pattern.match(line).group(3))
			processID_list.append(pattern.match(line).group(4))
			message_list.append(pattern.match(line).group(5))
			
			prv_date = current_date
			looped+=1
				

	uniq_process(proccess_list)
	host_names(hostname_list)
	top_messages(message_list)
	
	
def uniq_process(proccessList):
	"""Unique processes.

	"""

	uniq_list = collections.Counter(proccessList).most_common()
	print("Unique Proccess: ")
	for each in uniq_list:
		print("[{0:d}] {1:s}").format(each[1],each[0])
=======
	
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
>>>>>>> ac2c15e85a07012ffbe7491bf511d6ceb3cee872


def top_messages(messageList):
	"""List top 10 messages in the file.

	"""

	messages = collections.Counter(messageList).most_common(10)
	print("Top 10 Messages: ")
	for each in messages:
		print(each[0])


<<<<<<< HEAD
def host_names(hostnameList):
=======
def hostnames(hostnameList):
>>>>>>> ac2c15e85a07012ffbe7491bf511d6ceb3cee872
	"""Prints hostnames from list.

	"""
	
	hosts = collections.Counter(hostnameList)
	print("Hostsnames in file: ")
	for each in hosts:
		print(each)


if __name__ == '__main__':
	main()