import json
import shodan
import argparse
SHODAN_API_KEY = "<YOUR SHODAN API KEY HERE>"
api = shodan.Shodan(SHODAN_API_KEY)

parser = argparse.ArgumentParser(description='Get a list of IPs and return shodan info.')
parser.add_argument('--filename', '-f', default='iplist.txt')
args=parser.parse_args()

with open(args.filename, 'r') as f:
	ips = [line.strip() for line in f]


#print ips
awsInfo = {}
for ip in ips:
	try:
#		print ip
		hostinfo = api.host(ip)
		awsInfo[ip] = hostinfo
	except shodan.APIError, e:
		awsInfo[ip] = '{}'.format(e)

print json.dumps(awsInfo)
