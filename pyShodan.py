import shodan
import sys
import argparse
import csv
import time
import datetime

def getApiKey(k):
    SHODAN_API_KEY = k
    api = shodan.Shodan(SHODAN_API_KEY)
    return api

def searchTerm(s):
    searchStr = s
    api = getApiKey(args.apiKey)
    hostinfo = []
    # Wrap the request in a try/ except block to catch errors
    # Search Shodan
    results = api.search(searchStr)

    # Show the results
    print('Results found: %s' % results['total'])
    for result in results['matches']:
        print('IP: %s' % result['ip_str'])
        print(result['data'])
        print('')
        hostinfo.append([result['ip_str'].replace(","," "), result['data'].replace(","," ").encode("utf-8"),result['port']])

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
    try:
        host = api.host(searchHost)
        # Print general info
        print("""
            IP: %s
            Organization: %s
            Operating System: %s
            """ % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

        hostinfo = []

        for item in host['data']:
            hostinfo.append([item['ip_str'], item['org'], str(item['data'].replace(',',' ').strip('\t\n\r')), item['port']])
            print("""
                Port: %s
                Banner: %s
                """ % (item['port'], item['data']))
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
    hostinfo = []
    
    with open(f,'r') as dafile:
        x = dafile.read().splitlines()

    for i in range(len(x)):
        try:
            time.sleep(2)
            host = api.host(x[i])
            for item in host['data']:
                hostinfo.append([item['ip_str'], item['org'], str(item['data']).replace(',',' ').strip('\r\n\t'), item['port']])
        except shodan.APIError as e:
            print("Error: %s" % e)
            if "no information available" in str(e).lower():
                print("No information is available for %s" % str(x[i]))

    for i in range(len(hostinfo)):
        print("\n" + str(hostinfo[i]) + "\n")

    title = "shodanOutput-ipList-" + str(datetime.datetime.now()) + ".csv"
    with open(title,"w") as csvfile:
        header = ["Host IP", "FQDN", "Banner", "Ports"]
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(header)
        for i in range(len(hostinfo)):
            writer.writerow(hostinfo[i])
    
    print(title + " created in script directory")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python script for interacting with Shodan API")

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
