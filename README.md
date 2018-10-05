# pyShodan
Python 3 script for interacting with Shodan API. Has three modes of operation: making an API query for a search term, for a single IP address, or for a list of IP addresses in a .txt file.

## Installation
```
git clone https://github.com/GoVanguard/pyShodan.git
```

## Recommended Python Version
Supports Python 3.5+.

## Dependencies
* Shodan (pip3 install shodan)

## Usage
Short Form        | Long Form      | Description
----------------- | -------------- |-------------
-h                | --help         | show this help message and exit
-s                | --search       | Search Shodan for a general term
-ip               | --ipaddr       | Search Shodan for a specific IP address
                  | --iplist       | Search Shodan for every IP address in a txt file
-api              | --api          | Shodan API key (required)

Output is printed to stdout as well as CSV files in the script directory.
