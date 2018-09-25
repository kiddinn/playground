from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import datetime
import json
import os
import sys


def main():
    if not os.path.exists('Preferences'):
            print("Not a valid path")
            sys.exit
    else:
        with open('Preferences', 'rb') as fh:
            json_object = json.load(fh)
            print("Parsing chrome Preferences file")
            ChromePreferenceParser.parseName(json_object)
            ChromePreferenceParser.parseDate(json_object)
            ChromePreferenceParser.parseMedia(json_object)
            ChromePreferenceParser.parseExt(json_object)
            ChromePreferenceParser.parsePrint(json_object)


class ChromePreferenceParser(object):

    def _findIn(searchSpace, item):
        # Recursive search for items inside a nested dictionary
        foundItem = []
        try:
            for c, d in searchSpace.items():
                if c == item:
                    foundItem.append(d)
                else:
                    if isinstance(d, dict):
                        nestResult = findIn(d, item)
                        for result in nestResult:
                            foundItem.append(result)
                        else:
                            if isinstance(d, dict):
                                for nestedItems in d:
                                    if isinstance(nestedItems, dict):
                                        extraItems = findIn(nestedItems, item)
                                        for evenMoreItems in extraItems:
                                            foundItem.append(extraItems)
            return foundItem
        except Exception as e:
            print("Exception running application, here's what we know")
            print(e)
            return 0

    def _dateConversion(webkitTimestamp):
        # Converts date from webkit time to ISO 8601 time
        startDate = datetime.datetime(1601, 1, 1, 0, 0, 0, 0)
        currentDate = datetime.timedelta(microseconds=int(webkitTimestamp))
        isoTime = startDate + currentDate
        return isoTime

    def parseName():
        # Parse through and get the account name, email, and profile name
        # Returns the name, email and profile name
        try:

            for d in json_object['account_info']:
                name = d.get('full_name')
                email = d.get('email')
                for c in d['profile']:
                    profile = c.get('name')

                    return name, email, profile
        except Exception as e:
            print('Exception caught: ' + e)
            raise EnvironmentError.filename
            sys.exit

    def parseDate():
        # Parses the last time chrome was updated in ISO 8601 UTC format
        # Returns the last update date in ISO 8601 UTC
        try:

            webKitTime = json_object['last_update_date']
            finalDate = _dateConversion(webKitTime)
            return finalDate
        except Exception as e:
            print("Exception running application, here's what we know")
            print(e)
            return 0

    def parseMedia():
        # Parses the following information from the media_engagement key
        # 1: List of Websites 2: last modified 3. Media played? 4. visitcount
        # returns these keys in a dict
        try:
            media = {}
            for c, d in json_object['profile']['content_settings']['exceptions']['media_engagement'].iteritems():
                media.append(prefs.items(website=c, lastModified=dateConversion(d['last_modified']), playback=mediaPlaybacks, visitCount=visits))
                media.append(_dateConversion(media.webKitTime))
                return media
        except Exception as e:
            print("Exception running application, here's what we know")
            print(e)
            return 0

    def parseExt():
        # Gets a list of the current installed extensions and last update time
        # returns a list of extension ID's and the last update time in ISO 8601

        webKitTime = prefs.get(json_object['extensions']['autoupdate']['last_check'])
        _dateConversion(webKitTime)
        extensions = {}
        try:
            extList = findIn(json_object['extensions']['ids'])
            for d in extList:
                extensions.append(d)
            return extensions, endDate
        except Exception as e:
            print("Exception running application, here's what we know")
            print(e)
            return 0

    def parsePrint():
        # Creates a new JSON object and parses it to find currently installed printers
        # Returns a list of the currently installed printers in chrome
        printerList = {}
        newObject = json_object['printing']['print_preview_sticky_settings']['appState']
        new_json = json.JSONEncoder(newObject, encoding='utf-8', default=None)
        try:
            for c in new_json:
                printerList.append(c.get('selectedDestinationId'))
                return printerList
        except Exception as e:
            raise parseException

    def parseException():
        print("JSON parsing failed")

    if __name__ == "__main__":
            main()
