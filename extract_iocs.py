import re

with open("file.txt", "r") as file:
    data = file.read()

#Regex to find all emails, ips, and domains
email_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,63}\b'
domain_pattern = r'\b(?=.{4,253}\b)(?:[a-zA-Z0-9-]{1,63}\.)+[A-Za-z]{2,63}\b'
ip_pattern = r'\b(?:(?:25[0-5]|2[0-4]\d|1?\d?\d)(?:\.|$)){4}\b'

#Using re package to find them in the file 
emails = re.findall(email_pattern, data)
domains = re.findall(domain_pattern, data)
ips = re.findall(ip_pattern, data)