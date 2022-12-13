S=' -> '
R='domains.txt'
Q=open
A=print
import os,socket as E
from colorama import Fore as B,Back,Style as C
def L(strings):
	A=[]
	for B in strings:
		if B not in A:A.append(B)
	return A
F=R
G=os.path.exists(F)
A(B.CYAN+'# Name: Simple Mass Domain To IP')
A('# Author: Rahman Ralei')
A('# Script: Python3')
A('# Version: V1')
M=input('\nInput (y) untuk run program: '+C.RESET_ALL).lower()
H='-------------------------------------------------------------------------------'
if M=='y':
	if G==True:
		I=[];A(H);A(B.GREEN+'[!] Loading, Please Wait...\n'+C.RESET_ALL)
		with Q(R)as N:
			O=N.read().splitlines()
			for D in L(O):
				try:J=E.gethostbyname(D);A(B.YELLOW+f"{D}"+C.RESET_ALL+S+B.GREEN+f"{J}"+C.RESET_ALL);I.append(J)
				except E.gaierror:A(B.YELLOW+f"{D}"+C.RESET_ALL+S+B.RED+'Not Found!'+C.RESET_ALL)
		with Q('result-ip.txt','w')as P:
			K=''
			for (K,list) in enumerate(I):P.write(str(list)+'\n')
			A(B.CYAN+f"\n[!] Done!!!\n- Result IP : {K+1}\n- Ke simpen di file (result-ip.txt)"+C.RESET_ALL);A(H)
	if G==False:A(f"\nFile {F} gaada di directory lu! \nSilahkan buat filenya dulu di dalem directory yang sama.")
else:A('\nUpss Program telah terhenti!\nJika ingin menggunakan kembali silahkan buka kembali scriptnya.')
