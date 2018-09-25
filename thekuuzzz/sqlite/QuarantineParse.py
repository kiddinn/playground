from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from urlparse import urlsplit

import datetime
import os
import sqlite3


class QuarantineParse(object):
    """Parses the QuarantineEventsV2 file and prints domains + download agents

        Args:
        none

        Returns:
        none
    """

    def parseFile():
        agent_dict = dict(agent=' ', count=0)
        url_dict = dict(site=' ', count=0)
        try:
            database = sqlite3.connect('QuarantineEventsV2')
            database_query = database.execute('SELECT LSQuarantineTimestamp AS Time,
            LSQuarantineAgentName AS Agent, LSQuarantineOriginURLString AS URL,
            LSQuarantineDataURLString AS Data
            FROM LSQuarantineEvent ORDER BY Time;')
            for record in database_query.split('|'):
                if record.startswith(str.isdigit()):
                    time = _convert_time(record)
                elif record.startswith('https') | record.startswith('http'):
                    url = record
                    uri = urlsplit(record, scheme='', allow_fragments=True)
                    domain = '{uri.scheme}://{uri.netloc}/'
                    if domain not in url_dict:
                        url_dict[domain] = 1
                    else:
                        url_dict[domian] = url_dict[domain]+1
                    else:
                        if record not in agent_dict:
                            agent_dict[record] = 1
                        else:
                            agent_dict[record] = agent_dict[record]+1
                            source = record
            print(time + ' ' + source + ' downloaded from ' + url + '\n')
            print('List of Agents: ' + '\n')
            for agents, values in agent_dict:
                print(agent + ' -> ' + values)
            print('\n' + 'List of Domains: ' + '\n')
            for domains, values in url_dict:
                print(domains + ' -> ' + values)
        except EnvironmentError as e:
            print('I/O error with database file' + e)
        except EOFError as eof:
            print('Parser reached end of file and didnt expect it' + eof)
        except Exception as eek:
            print("Look at this exception isnt it wonderful" + eek)

    """ Helper method to convert from cocoa to ISO time

    Args:
     cocoa timestamp

    Returns:
     ISO 8601 timestamp

    """
    def _convert_time(cocoa_time):
        try:
            start_time = datetime.datetime(2001, 1, 1, 0, 0, 0, 0)
            current_time = datetime.timedelta(microseconds=int(cocoa_time))
            new_time = start_time + current_time
            new_time = datetime.datetime.isoformat(new_time)
            return new_time
        except exception as e:
            print "Look at this exception isnt it wonderful" + e
