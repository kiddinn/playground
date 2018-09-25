from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import ChromePreferenceParser


class ArgParser(object):

    def __init__(self):
        parser = argparse.ArgumentParser(description='Parse 3 types of files')
        parser.add_argument('--name', '-n', action='store', help='Returns the name, email, and profile name')
        parser.add_argument('--date', '-d', action='store', help='Returns the last time chrome updated in ISO 8601 UTC')
        parser.add_argument('--media', '-m', action='store', help='Returns a list of websites and information about them')
        parser.add_argument('--ext', '-e', action='store', help='returns a list of extension IDs and the last update time in ISO 8601')
        parser.add_argument('--printer', '-p', action='store', help='Returns a list of the users currently installed printers')
        parser.add_argument('file', type=file, help=' A file that needs to be parsed')
        args = vars(parser.parse_args())

    def fileCheck(self):
        if args[file]
