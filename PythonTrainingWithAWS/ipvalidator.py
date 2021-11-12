
#!/usr/bin/python3

import subprocess
import sys
import os
import re

def ipvalidator(IPv4_address_as_string):
    """returns True if address is a valid dotted-quad, False otherwise."""

    # Ensure we have a dotted quad address
    r = re.search(r'^(\d+)\.(\d+)\.(\d+)\.(\d+)$', IPv4_address_as_string)
    if r:
        # test each number in dotted quad
        for quad in r.groups():
            if int(quad) > 255:
                return False
    else:
        # no match
        return False

    # all good
    return True


def ping_validator(IPv4_address_as_string):
    """ ping ip and returns True if ping successful, False otherwise."""
    if ipvalidator(IPv4_address_as_string):
        p = subprocess.run(("ping", "-c", "1", IPv4_address_as_string), stdout=subprocess.DEVNULL)
        return True if p.returncode == 0 else False
    else:
        return False


if __name__=="__main__":

    print(ipvalidator("192.168.200.204"))
    print(ipvalidator("192.168.200.254"))
    print(ipvalidator("111.111.11.1"))
    print(ipvalidator("666.666.666.666"))

    print("ping: 192.168.200.204")
    print(ping_validator("192.168.200.204"))
    print("ping: 192.168.200.254")
    print(ping_validator("192.168.200.254"))
    print("ping: 666.666.666.666")
    print(ping_validator("666.666.666.666"))
    print("ping: 111.111.11.1")
    print(ping_validator("111.111.11.1"))
    print("ping: 8.8.8.8")
    print(ping_validator("8.8.8.8"))
