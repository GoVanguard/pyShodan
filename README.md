pyShodan (https://gotham-security.com)
==
[![Python package](https://github.com/GoVanguard/pyShodan/actions/workflows/master.yml/badge.svg)](https://github.com/GoVanguard/pyShodan/actions/workflows/master.yml)
[![Known Vulnerabilities](https://snyk.io/test/github/GoVanguard/pyShodan/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/GoVanguard/pyShodan?targetFile=requirements.txt)
[![Maintainability](https://api.codeclimate.com/v1/badges/6b69cfa99c674d04e7a9/maintainability)](https://codeclimate.com/github/GoVanguard/pyShodan/maintainability)

# About pyShodan
Python 3 script for interacting with Shodan API. Has three modes of operation: making an API query for a search term, a single IP address, or for a list of IP addresses in a .txt file.

## Installation
```
git clone https://github.com/GoVanguard/pyShodan.git
```

## Recommended Python Version
Tested on Python 3.6+.

## Dependencies
* Shodan (pip3 install shodan)

Output is printed to stdout as well as CSV files in the script directory.
