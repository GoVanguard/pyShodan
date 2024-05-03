from . import PyShodan
import shodan
import sys
import argparse
import csv
import time
import datetime

def getApiKey(k):
    api = k
    return api

def writeFile(t, h):
    with open(t,"w") as csvfile:
        header = ["Host IP", "FQDN", "Banner", "Ports"]
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(header)
        for i in range(len(h)):
            writer.writerow(h[i])
    print(t + " created in script directory")

def searchTerm(s):
    searchStr = s
    api = getApiKey(args.apiKey)
    ps = PyShodan()
    ps.apiKey = api
    ps.createSession()
    hostinfo = ps.searchTerm(searchStr)
    title = "shodanOutput-" + searchStr + ".csv"
    writeFile(title, hostinfo)

def searchIp(d):
    searchHost = d
    api = getApiKey(args.apiKey)
    ps = PyShodan()
    ps.apiKey = api
    ps.createSession()
    try:
        hostinfo = ps.searchIp(searchHost)
        title = "shodanOutput-" + searchHost + ".csv"
        writeFile(title, hostinfo)
    except shodan.APIError as e:
        print("Error: %s" % e)

def searchList(f):
    api = getApiKey(args.apiKey)
    ps = PyShodan()
    ps.apiKey = api
    ps.createSession()
    d = datetime.datetime.today()
    hostinfo = ps.searchList(f)
    title = "shodanOutput-ipList_" + d.strftime("%d-%m-%Y_%H-%M-%S") + ".csv"
    writeFile(title, hostinfo)

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
