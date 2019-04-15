import subprocess

interface = input("Değiştirmek İstediğiniz Interface Girin : ")

secim = input("""
1 - Random Mac
2 - Default Mac

""")

subprocess.call(["ifconfig",interface,"down"])

if (secim=="1"):
    subprocess.call(["macchanger","-r",interface])
elif (secim=="2"):
    subprocess.call(["macchanger","-p",interface])
else:
    print("HATA")

subprocess.call(["ifconfig",interface,"up"])