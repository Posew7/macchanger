import re
import subprocess

def deneme():


    ifconfig = subprocess.check_output(["ifconfig","eth0"])

    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)

    if new_mac:
        return new_mac.group(0)
    else:
        return None

new = deneme()

print(new)
