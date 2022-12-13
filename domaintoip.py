R=' => '
Q='domains.txt'
P=open
A=print
import os,socket as G
from colorama import Fore as B,Back,Style as C
def H(strings):
	A=[]
	for B in strings:
		if B not in A:A.append(B)
	return A
I=Q
J=os.path.exists(I)
A(B.CYAN+'# Name: Simple Mass Domain To IP')
A('# Author: Rahman Ralei')
A('# Script: Python3')
A('# Version: V1')
L=input('\n# Input (y) untuk run program: '+C.RESET_ALL).lower()
K='-------------------------------------------------------------------------------'
if L=='y':
	if J==True:
		D=[];A(K);A(B.GREEN+'[!] Loading, Please Wait...\n'+C.RESET_ALL)
		with P(Q)as M:
			N=M.read().splitlines()
			for F in H(N):
				try:E=G.gethostbyname(F);A(B.YELLOW+f"{F}"+C.RESET_ALL+R+B.GREEN+f"{E}"+C.RESET_ALL);D.append(E)
				except G.gaierror:A(B.YELLOW+f"{F}"+C.RESET_ALL+R+Back.RED+'Not Found!'+C.RESET_ALL)
		with P('result-ip.txt','w')as O:
			D=list(H(D))
			for (E,list) in enumerate(D):O.write(str(list)+'\n')
			A(B.CYAN+f"""
# Done!
# Total IP + Remove Duplicate : {E+1}
# Saved (result-ip.txt)"""+C.RESET_ALL);A(K)
	if J==False:A(f"\nFile {I} gaada di directory lu! \nSilahkan buat filenya dulu di dalem directory yang sama.")
else:A('\nUpss Program telah terhenti!\nJika ingin menggunakan kembali silahkan buka kembali scriptnya.')
