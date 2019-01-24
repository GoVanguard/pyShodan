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

from pyShodan import pyShodan
import sys
import argparse
import csv
import time
import datetime

def getApiKey(k):
    api = k
    return api

def searchTerm(s):
    searchStr = s
    api = getApiKey(args.apiKey)
    ps = pyShodan(api, False)
    hostinfo = ps.searchTerm(searchStr)

    title = "shodanOutput-" + searchStr + ".csv"
    with open(title,"w") as csvfile:
        header = ["Host IP", "Banner","Ports"]
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(header)
        for i in range(len(hostinfo)):
            writer.writerow(hostinfo[i])

    print(title + " created in script directory")

def searchIp(d):
    searchHost = d
    api = getApiKey(args.apiKey)
    ps = pyShodan(api, False)
    try:
        hostinfo = ps.searchIp(searchHost)

        title = "shodanOutput-" + searchHost + ".csv"
        with open(title,"w") as csvfile:
            header = ["Host IP", "FQDN", "Banner", "Ports"]
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerow(header)
            for i in range(len(hostinfo)):
                writer.writerow(hostinfo[i])

        print(title + " created in script directory")
    except shodan.APIError as e:
        print("Error: %s" % e)

def searchList(f):
    api = getApiKey(args.apiKey)
    hostinfo = ps.searchList(f)
    with open(f,'r') as dafile:
        x = dafile.read().splitlines()

    title = "shodanOutput-ipList-" + str(datetime.datetime.now()) + ".csv"
    with open(title,"w") as csvfile:
        header = ["Host IP", "FQDN", "Banner", "Ports"]
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(header)
        for i in range(len(hostinfo)):
            writer.writerow(hostinfo[i])
    
    print(title + " created in script directory")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="pyShodan test script")

    parser.add_argument("--search", "-s", action="store", type=str, dest="searchVal", help="Search Shodan for a general term")
    parser.add_argument("--ipaddr", "-ip", action="store", type=str, dest="ipSearch", help="Search Shodan for a specific IP address")
    parser.add_argument("--iplist", action="store", dest="ipList", help="Search Shodan for every IP address in a txt file")
    parser.add_argument("--api", "-api", action="store", type=str, dest="apiKey", required=True, help="Shodan API key")
    args = parser.parse_args()

    if args.searchVal:
        searchTerm(args.searchVal)
    elif args.ipSearch:
        searchIp(args.ipSearch)
    elif args.ipList:
        searchList(args.ipList)
    elif args.apiKey:
        getApiKey(apiKey)
    else:
        print("Invalid arguments, see -h for details. Example use: python pyShodan.py -s SearchTerm -ip IPAddress -api SHODAN-api-key")
