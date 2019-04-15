import subprocess
import optparse

def get_user_input():
    parse = optparse.OptionParser()

    parse.add_option("-i","--interface",dest="interface",help="change to interface")
    parse.add_option("-m","--mac",dest="mac_address",help="new mac address")

    return parse.parse_args()

def change_mac_address(interface,mac_address):

    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac_address])
    subprocess.call(["ifconfig",interface,"up"])

def control_new_mac(interface):

    ifconfig = subprocess.check_output(["ifconfig",interface])
    print(ifconfig)

(user_inputs,arguments) = get_user_input()
change_mac_address(user_inputs.interface,user_inputs.mac_address)
control_new_mac(user_inputs.interface)