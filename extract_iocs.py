import re
import ipaddress
import json

with open("file.txt", "r") as file:
    data = file.read()

#Regex to find all emails, ips, and domains
email_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,63}\b'
domain_pattern = r'\b(?=.{4,253}\b)(?:[a-zA-Z0-9-]{1,63}\.)+[A-Za-z]{2,63}\b'
ip_pattern = r'[0-9]+(?:\.[0-9]+){3}'

#Using re package to find them in the file 
emails = re.findall(email_pattern, data)
domains = re.findall(domain_pattern, data)
ips = re.findall(ip_pattern, data)

#Find out which ipaddresses are valid in order to add them to a json file
valid_ips = []
for ip in ips:
    try:
        ipaddress.IPv4Address(ip)
        valid_ips.append(ip)
    except ipaddress.AddressValueError:
        pass

emails = list(set(emails))
domains = list(set(domains))
valid_ips = list(set(valid_ips))

json_data = {
    "ips": valid_ips,
    "domains": domains,
    "emails": emails
}

with open("info.json", "w") as outfile:
    json.dump(json_data, outfile, indent=4)