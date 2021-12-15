import json
import shodan
import argparse
from dotenv import load_dotenv
import time
import rich
import os
from rich import print

load_dotenv()

SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")
api = shodan.Shodan(SHODAN_API_KEY)

parser = argparse.ArgumentParser(description='Get a list of IPs and return shodan info.')
parser.add_argument('--filename', '-f', default='iplist.txt')
argsc = parser.parse_args()

with open(argsc.filename, 'r') as f:
    ips = [line.strip() for line in f]

ipInfo = {}
for ip in ips:
    try:
        hostinfo = api.host(ip)
        ipInfo[ip] = hostinfo
        time.sleep(1)
    except shodan.APIError as e:
        ipInfo[ip] = '{}'.format(e)

print(json.dumps(ipInfo))
