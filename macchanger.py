import subprocess

print("""
1 - Random Mac
2 - Default Mac
""")

secim = input("Yapmak İstediğiniz İşlemi Seçin : ")
print("")
interface = input("Değiştirmek İstediğiniz Interface Girin : ")
print("")
subprocess.call(["ifconfig",interface,"down"])
if (secim=="1"):
    subprocess.call(["macchanger","-r",interface])
else:
    subprocess.call(["macchanger","-p",interface])
subprocess.call(["ifconfig",interface,"up"])