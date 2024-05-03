import shodan
import sys
import time
from IPy import IP
from typing import List, Union, Tuple


class PyShodan:

    def __init__(self, apiKey: str = None, debug: bool = False):
        self.apiKey = apiKey
        self.debug = debug
        self.shodanSession = None

    def createSession(self) -> Union[None, str]:
        if self.apiKey:
            self.shodanSession = shodan.Shodan(self.apiKey)
        else:
            return 'Set API Key'

    def searchTerm(self, searchStr: str, allData: bool = False) -> Union[List[dict], str]:
        if not self.shodanSession:
            return 'Set API Key'

        if not searchStr:
            return 'No search input'

        try:
            apiResult = self.shodanSession.search(searchStr)
            print(f'Results found: {apiResult["total"]}')

            if allData:
                return apiResult['matches']
            else:
                return [[result['ip_str'], result['data'], result['port']] for result in apiResult['matches']]
        except shodan.APIError as e:
            return f"Error: {e}"

    def searchIp(self, searchHost: str, allData: bool = False) -> Union[List[dict], str]:
        if not self.shodanSession:
            return 'Set API Key'

        if not searchHost:
            return 'No search input'

        searchHostIpType = IP(searchHost).iptype()

        if searchHostIpType != "PUBLIC":
            return f"Warning, {searchHost} isn't public. Shodan only tracks public IPs."

        try:
            apiResult = self.shodanSession.host(searchHost)

            if allData:
                return apiResult
            else:
                return [[item['ip_str'], item['org'], item['data'].replace(',', ' ').strip(), item['port']] for item in apiResult['data']]
        except shodan.APIError as e:
            return f"Error: {e}"

    def searchList(self, inputFile: str) -> Union[List[dict], str]:
        if not self.shodanSession:
            return 'Set API Key'

        if not inputFile:
            return 'No input file'

        try:
            with open(inputFile, 'r') as f:
                ips = f.read().splitlines()

            hostInfo = []
            for ip in ips:
                time.sleep(2)
                try:
                    host = self.shodanSession.host(ip)
                    for item in host['data']:
                        hostInfo.append([item['ip_str'], item['org'], item['data'].replace(',', ' ').strip(), item['port']])
                except shodan.APIError as e:
                    if "no information available" in str(e).lower():
                        print(f"No information is available for {ip}")
                    else:
                        print(f"Error: {e}")

            return hostInfo
        except Exception as e:
            return f"Error while reading file: {e}"
