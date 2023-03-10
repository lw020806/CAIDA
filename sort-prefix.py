import sys
import random
import ipaddress as ipad
from ipaddress import ip_network

continents = ["NA", "SA", "AS", "EU", "AF", "OC"]
continents_asn = {}
unrecognized_asn = set()

asnSortedFileName = "asn-sorted/asn_sorted.txt"
with open(asnSortedFileName, 'r') as asnSortedFile:
    for line in asnSortedFile:
        line = line.rstrip("\n")
        line = line.split()
        asns = set()
        for i in range(1, len(line)):
            asns.add(line[i])
        continents_asn[line[0]] = asns
    
interest = sys.argv[1]
prefixes = []

pfx2asFileName = "raw-data/routeviews-rv2-20230301-1200.pfx2as"
with open(pfx2asFileName, 'r') as fpx2asFile:
    for line in fpx2asFile :
        line = line.rstrip("\n").split()
        ip = line[0]
        len = line[1]
        asn = line[2]
        continent = ""

        if asn in continents_asn[interest] : # and int(len) <= 16:
            prefixes.append(ip+"/"+len)
            # for subnet in list(ip_network(ip+"/"+len).subnets(new_prefix=16)) :
            #     prefixes.append(subnet)
        else :
            unrecognized_asn.add(asn)

# random.shuffle(prefixes)
for prefix in prefixes :
    print(prefix)
# print("error unrecognized asn:", unrecognized_asn)
