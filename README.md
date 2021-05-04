# Shodan Bulk IP Query
This tool gets a list of IPs in a file (one IP per line) and queries shodan.io. It prints the query results in JSON format to stdout. 

# Prerequisite
* `pip install -r requirements.txt`
* Define your SHODAN_API_KEY in a file called `.env` in the root directory of the app.
* Get your IPs in a file \n separated. See `iplist.txt` file for an example. 

# Usage
`# python ipQuery.py` will take as default filename: `iplist.txt` as filename to read the IPs from. You can always use `-f` or `--filename` as an argument to provide your filename. 

`# python ipQuery.py -f myawesomepath/myawesomefilename.foo`


# TODO
- Throttling for big queries.
- Combine IPs to make one bulk query.
