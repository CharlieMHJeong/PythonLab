#!/usr/bin/python3

import xml.dom.minidom
import xml.etree.ElementTree as ET
import sys
import json

from xml.dom.minidom import parse
from ipvalidator import ipvalidator

def xml2dict(filein):

    system_d = {}

    ##root.tag ==> system
    systems = ET.parse(filein).getroot()
    #print(systems.tag)
    ping_l = []

    for host in systems:
        #print(host)
        #print(f"hosttag: {host.tag}, hostattrib: {host.attrib}")
        host_d = {}
        ping_d = {}
        for ipjob in host:
            #print(f"ip.tag: {ipjob.tag}, ip.text: {ipjob.text}")
            #ping_l = []
            #ping_d = {}

            if ipjob.tag == 'ip':
                #ipjob.text is ipaddr
                system_d[ipjob.text] = []
                host_l = system_d[ipjob.text]
                if ipvalidator(ipjob.text):
                    ping_d["ip"] = ipjob.text
                    ping_d["success"] = True
                    ping_l.append(ping_d)
                else:
                    ping_d["ip"] = ipjob.text
                    ping_d["success"] = False
                    ping_l.append(ping_d)

            if ipjob.tag == 'job':
                job_d = {}
                for child in ipjob:
                    job_d[child.tag] = child.text
                host_l.append(job_d)

       # print("Pinging now")

    #python list[dict{}]
    #print(ping_l)
    #printout in json format
    print()
    print("*"*80)
    print(json.dumps(ping_l))

    return system_d


def extract_XML_data(filename):
    """Read XML data in filename, return a collection"""
    coll = {}

    # walk the XML tree.
    # for each IP address, extract command & comment
    root = xml.dom.minidom.parse(filename)
    systems = root.documentElement
    hosts = systems.getElementsByTagName("host")
    for host in hosts:
        ips = host.getElementsByTagName("ip")
        ip_address = ips[0].childNodes[0].data

        # do not add invalid IPs to collection
        if not ipvalidator(ip_address):
            continue

        # each new IP is a new key in collection
        coll[ip_address] = []

        jobs = host.getElementsByTagName("job")
        for job in jobs:
            commands = job.getElementsByTagName("command")
            for command in commands:
                # print("/system/host/ip={}/job/command={}".format(ip_address, command.childNodes[0].data))
                cmd = command.childNodes[0].data
            comments = job.getElementsByTagName("comment")
            for comment in comments:
                # print("/system/host/ip={}/job/comment={}".format(ip_address, comment.childNodes[0].data))
                cmt = comment.childNodes[0].data

            # append this job to the IP address
            coll[ip_address].append({"command":cmd, "comment":cmt})

    return coll



if __name__=="__main__":

    print(xml2dict(sys.argv[1]))
    print()
    ex = extract_XML_data(sys.argv[1])
    import pprint
    pprint.pprint(ex)
