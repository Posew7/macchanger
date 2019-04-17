#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import optparse
import re


def user_input():
    parse = optparse.OptionParser()
    parse.add_option("-i","--interface",dest="interface",help="change to interface")
    parse.add_option("-m","--mac",dest="mac_address",help="new mac address")

    return parse.parse_args()

def change_mac(interface,mac_address):
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
    subprocess.call(["ifconfig",interface,"up"])

def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)

    if (new_mac):
        return new_mac.group(0)
    else:
        return None


(user_inputs,arguments) = user_input()
change_mac(user_inputs.interface,user_inputs.mac_address)
final_mac = control_new_mac(user_inputs.interface)

if final_mac == user_inputs.mac_address:
    print ("başarılı yeni mac : "+final_mac)
else:
    print ("başarısız mac değişmedi")