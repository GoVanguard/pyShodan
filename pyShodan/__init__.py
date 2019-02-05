#####################################################################################
#                  pyShodan: Python API Wrapper for Shodan                          #
#                       Copyright (c) 2019 GoVanguard                               #
#####################################################################################
# This file is part of pyShodan.                                                    #
#                                                                                   #
#     pyShodan is free software: you can redistribute it and/or modify              #
#     it under the terms of the GNU Lesser General Public License as published by   #
#     the Free Software Foundation, either version 3 of the License, or             #
#     (at your option) any later version.                                           #
#                                                                                   #
#     pyShodan is distributed in the hope that it will be useful,                   #
#     but WITHOUT ANY WARRANTY; without even the implied warranty of                #
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                 #
#     GNU Lesser General Public License for more details.                           #
#                                                                                   #
#     You should have received a copy of the GNU Lesser General Public License      #
#     along with pyShodan.  If not, see <http://www.gnu.org/licenses/>.             #
#####################################################################################

import shodan
import sys

class pyShodan:

    #Constructor
    def __init__(self, apiToken: str, debug=False):
        self.__api = shodan.Shodan(apiToken)
        self.__debug = debug

    def debug(self, val: bool):
        self.__debug = val

    def searchTerm(self, searchStr: str):
        api = self.__api
        hostinfo = []

        # Search Shodan for this term
        results = api.search(searchStr)

        # Format the results into list
        print('Results found: %s' % results['total'])
        for result in results['matches']:
            hostinfo.append([result['ip_str'].replace(","," "), result['data'].replace(","," ").encode("utf-8"),result['port']]) # Store the results in a list

        return hostinfo

    def searchIp(self, searchHost: str):
        api = self.__api
        hostinfo = []

        # Search Shodan for this IP address
        try:
            host = api.host(searchHost)

            for item in host['data']:
                hostinfo.append([item['ip_str'], item['org'], str(item['data'].replace(',',' ').strip('\t\n\r')), item['port']]) # Store the results in a list

        except shodan.APIError as e:
            print("Error: %s" % e)

        return hostinfo

    def searchList(self, f: str):
        api = self.__api
        hostinfo = []

        # Open the file containing a list of IP addresses
        with open(f,'r') as dafile:
            x = dafile.read().splitlines()

        # Iterate through lines in the file
        for i in range(len(x)):
            try:
                time.sleep(2)
                host = api.host(x[i]) # Search Shodan for the host on the current line in the file
                for item in host['data']:
                    hostinfo.append([item['ip_str'], item['org'], str(item['data']).replace(',',' ').strip('\r\n\t'), item['port']]) # Store the results in a list
            except shodan.APIError as e:
                print("Error: %s" % e)
                if "no information available" in str(e).lower():
                    print("No information is available for %s" % str(x[i]))

        return hostinfo
