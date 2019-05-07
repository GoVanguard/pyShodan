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
import time
from IPy import IP

class PyShodan:

    #Constructor
    def __init__(self):
        self.apiKey = None
        self.debug = False
        self.shodanSession = None

    def createSession(self):
        if self.apiKey:
            self.shodanSession = shodan.Shodan(self.apiKey)
            return
        else:
            return 'Set API Key'

    def searchTerm(self, searchStr: str, allData = False):
        if not self.shodanSession:
            return 'Set API Key'

        if not searchHost:
            return 'No search input'

        hostResult = []

        # Search Shodan for this term
        apiResult = self.shodanSession.search(searchStr)

        # Format the results into list
        print('Results found: %s' % results['total'])

        if allData == True:
            hostResult = apiResult['matches']
        else:
            for result in apiResult['matches']:
                hostResult.append([result['ip_str'].replace(","," "), result['data'].replace(","," ").encode("utf-8"),result['port']]) # Store the results in a list

        return hostResult

    def searchIp(self, searchHost: str, allData = False):
        if not self.shodanSession:
            return 'Set API Key'

        if not searchHost:
            return 'No search input'

        searchHostIpType = IP(searchHost).iptype()

        if searchHostIpType != "PUBLIC":
            return "Warning, {0} isn't public.. Shodan only tracks public IPs".format(searchHost)

        hostResult = []

        # Search Shodan for this IP address
        try:
            apiResult = self.shodanSession.host(searchHost)

            if allData == True:
                hostResult = apiResult
            else:
                for item in apiResult['data']:
                    hostResult.append([item['ip_str'], item['org'], str(item['data'].replace(',',' ').strip('\t\n\r')), item['port']]) # Store the results in a list

        except shodan.APIError as e:
            print("Error: %s" % e)

        return hostResult

    def searchList(self, inputFile: str):
        if not self.shodanSession:
            return 'Set API Key'

        if not inputFile:
            return 'No inout file'

        hostinfo = []

        # Iterate through lines in the file
        for i in range(len(inputFile.read().splitlines())):
            try:
                time.sleep(2)
                host = self.shodanSession.host(x[i]) # Search Shodan for the host on the current line in the file
                for item in host['data']:
                    hostinfo.append([item['ip_str'], item['org'], str(item['data']).replace(',',' ').strip('\r\n\t'), item['port']]) # Store the results in a list
            except shodan.APIError as e:
                print("Error: %s" % e)
                if "no information available" in str(e).lower():
                    print("No information is available for %s" % str(x[i]))

        return hostinfo
