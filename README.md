pyShodan (https://govanguard.io)
==
[![Build Status](https://travis-ci.com/GoVanguard/pyShodan.svg?branch=master)](https://travis-ci.com/GoVanguard/pyShodan)
[![Known Vulnerabilities](https://snyk.io/test/github/GoVanguard/pyShodan/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/GoVanguard/pyShodan?targetFile=requirements.txt)
[![Maintainability](https://api.codeclimate.com/v1/badges/6b69cfa99c674d04e7a9/maintainability)](https://codeclimate.com/github/GoVanguard/pyShodan/maintainability)

# About pyShodan
Python 3 script for interacting with Shodan API. Has three modes of operation: making an API query for a search term, for a single IP address, or for a list of IP addresses in a .txt file.

## Installation
```
git clone https://github.com/GoVanguard/pyShodan.git
```

## Recommended Python Version
Tested on Python 3.5+.

## Dependencies
* Shodan (pip3 install shodan)

## Usage
Short Form        | Long Form      | Description
----------------- | -------------- |-------------
-h                | --help         | show this help message and exit
-s                | --search       | Search Shodan for a general term
-ip               | --ipaddr       | Search Shodan for a specific IP address
n/a               | --iplist       | Search Shodan for every IP address in a txt file
-api              | --api          | Shodan API key (required)

Output is printed to stdout as well as CSV files in the script directory.
