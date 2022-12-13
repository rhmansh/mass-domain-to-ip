import os
import socket
from colorama import Fore, Back, Style

path = "domains.txt"
exs = os.path.exists(path)
print(Fore.CYAN+"# Name: Simple Mass Domain To IP")
print("# Author: Rahman Ralei")
print("# Script: Python3")
print("# Version: V1")
ah = input("\nInput (y) untuk run program: "+Style.RESET_ALL).lower()
grs = "-------------------------------------------------------------------------------"
if(ah == "y"):
    if exs == True:
    	res = []
    	print(grs)
    	print(Fore.GREEN+"[!] Loading, Please Wait...\n"+Style.RESET_ALL)
    	with open("domains.txt") as f:
    		daftar_domain = f.read().splitlines()
    		for domain in daftar_domain:
    		   	try:
    		   		ip = socket.gethostbyname(domain)
    		   		print(Fore.YELLOW+f"{domain}"+Style.RESET_ALL+" -> "+Fore.GREEN+f"{ip}"+Style.RESET_ALL)
    		   		res.append(ip)  		
    		   	except socket.gaierror:
    		   		print(Fore.YELLOW+f"{domain}"+Style.RESET_ALL+" -> "+Fore.RED+"Not Found!"+Style.RESET_ALL)
    	with open("result-ip.txt", "w") as sv:
    		cnt = ""
    		for cnt, list in enumerate(res):
    			sv.write(str(list)+"\n")
    		print(Fore.CYAN+f"\n[!] Done!!!\n- Result IP : {cnt + 1}\n- Ke simpen di file (result-ip.txt)"+Style.RESET_ALL)
    		print(grs)
    if exs == False:
    	print(f"\nFile {path} gaada di directory lu! \nSilahkan buat filenya dulu di dalem directory yang sama.")
else:
	print('\nUpss Program telah terhenti!\nJika ingin menggunakan kembali silahkan buka kembali scriptnya.')