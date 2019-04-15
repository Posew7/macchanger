import subprocess
import optparse

parse = optparse.OptionParser()
parse.add_option("-i","--interface",dest="interface",help="interface to change")
parse.add_option("-m","--mac",dest="mac",help="new mac adress")

(user_inputs,arguments) = parse.parse_args()

interface = user_inputs.interface
mac = user_inputs.mac

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",mac])
subprocess.call(["ifconfig",interface,"up"])