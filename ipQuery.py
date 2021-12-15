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
parser.add_argument('--delay', '-d', default=0, type=int)
parser.add_argument('--verbose', '-v', default=True)
parser.add_argument('--output', '-o', default=None)

argsc = parser.parse_args()

with open(argsc.filename, 'r') as f:
    ips = [line.strip() for line in f]

ipInfo = {}
for ip in ips:
    if argsc.verbose:
        print(f'[INFO] - fetching host {ip}') 
    try:
        hostinfo = api.host(ip)
        ipInfo[ip] = hostinfo
        time.sleep(argsc.delay)
    except shodan.APIError as e:
        if argsc.verbose:
            print(f'[ERROR] - fetching host {ip}', e)
        ipInfo[ip] = '{}'.format(e)
# default=f'shodan_results_{int(time.time())}.json'
print(json.dumps(ipInfo))
if argsc.output != None:
    ofname = argsc.output
    with open(ofname, 'w') as of:
        of.write(json.dumps(ipInfo))
    print(f'[INFO] output written to {ofname}')
