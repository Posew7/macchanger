import subprocess

mac = input("Yeni Mac Adresini Girin : ")
interface = input("Değiştirmek İstediğin Interface Girin : ")

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",mac])
subprocess.call(["ifconfig",interface,"up"])