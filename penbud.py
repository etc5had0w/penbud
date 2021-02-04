#!/usr/bin/python3

import os,sys,subprocess,time,pkg_resources

RESET = '\033[m' # reset to the defaults
BackgroundBlack = "\033[40m"
Black        = "\033[30m"
Red          = "\033[31m"
Green        = "\033[32m"
Yellow       = "\033[33m"
Blue         = "\033[34m"
Magenta      = "\033[35m"
Cyan         = "\033[36m"
LightGray    = "\033[37m"
DarkGray     = "\033[90m"
LightRed     = "\033[91m"
LightGreen   = "\033[92m"
LightYellow  = "\033[93m"
LightBlue    = "\033[94m"
LightMagenta = "\033[95m"
LightCyan    = "\033[96m"
White        = "\033[97m"
Blink      = "\033[5m"
BOLD = '\033[1m'


def logo():
	print(BOLD+BackgroundBlack+Yellow +"---------------------------------------------------"+RESET)
	print(BOLD+BackgroundBlack+Yellow +"---------------------------------------------------"+RESET)
	print(BackgroundBlack+Yellow +"██████╗ ███████╗███╗   ██╗██████╗ ██╗   ██╗██████╗ "+RESET)
	print(BackgroundBlack+Yellow +"██╔══██╗██╔════╝████╗  ██║██╔══██╗██║   ██║██╔══██╗"+RESET)
	print(BackgroundBlack+Yellow +"██████╔╝█████╗  ██╔██╗ ██║██████╔╝██║   ██║██║  ██║"+RESET)
	print(BackgroundBlack+Yellow +"██╔═══╝ ██╔══╝  ██║╚██╗██║██╔══██╗██║   ██║██║  ██║"+RESET)
	print(BackgroundBlack+Yellow +"██║     ███████╗██║ ╚████║██████╔╝╚██████╔╝██████╔╝"+RESET)
	print(BackgroundBlack+Yellow +"╚═╝     ╚══════╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚═════╝ "+RESET)
	print(BOLD+BackgroundBlack+Yellow +"---------------------------------------------------"+RESET)
	print(BOLD+BackgroundBlack+Yellow +"----- Your Personal Penetration Tester Buddy ------"+RESET) 
	print(BOLD+BackgroundBlack+Yellow +"---------------------------------------------------"+RESET)
	print(BOLD+BackgroundBlack+Green+"Author : Himanshu Shukla --------------------------\n"+RESET)  
	time.sleep(1)                                              	



def toolcheck():

	print(BOLD+Cyan+"---------------------------------------------------"+RESET)
	print(BOLD+Cyan+"---------- Checking Availablity of Tools ----------"+RESET) 
	print(BOLD+Cyan+"---------------------------------------------------"+RESET)

	tools=['nmap','gobuster','nikto','john','hashcat','msfvenom']
	for i in tools:
		time.sleep(0.5)
		NOECHO = open(os.devnull, 'w')
		output = subprocess.call(["which", i], stdout=NOECHO, stderr=subprocess.STDOUT)
		if output==0:
			print(BOLD+Green+"[+] "+i+" is Available."+RESET)
		else:
			print(BOLD+Red+"[-] "+i+" is Not Installed! "+RESET+BOLD+Cyan+"(Install Using This command : apt-get install "+i+" )")
	


def mainmenu():

	time.sleep(1)
	print(BOLD+Cyan+"---------------------------------------------------"+RESET)
	print(BOLD+Cyan+"-------------------- Main Menu --------------------"+RESET) 
	print(BOLD+Cyan+"---------------------------------------------------\n"+RESET)
	print(BOLD+Cyan+"1.Reconnaissance \n2.Hash Cracking \n3.Payload Creation \n4.File Transfers\n")
	print(BOLD+Green+"[+] Use Index Number As Input.\n"+RESET)
	m1=input(BOLD+Green+"input"+Blink+" > "+RESET)
	
	
	if m1=='1':
		os.system('clear')
		print(BOLD+Cyan+"------------- Reconnaissance ------------\n"+RESET)
		print(BOLD+Cyan+"1.nmap \n2.gobuster \n3.nikto\n"+RESET)
		print(BOLD+Cyan+"[+] Use Index Number As Input.\n"+RESET)
		m2=input(BOLD+Green+"input"+Blink+" > "+RESET)

		if m2=='1':
			os.system('clear')
			
			recon.nmap()

		if m2=='2':
			os.system('clear')
			
			recon.gobuster()

		if m2=='3':
			os.system('clear')
			
			recon.nikto()

	if m1=='2':
		os.system('clear')
		print(BOLD+Cyan+"------------- Hash Cracking ------------\n"+RESET)
		print(BOLD+Cyan+"1.john \n2.hashcat \n"+RESET)
		print(BOLD+Cyan+"[+] Use Index Number As Input.\n"+RESET)
		m2=input(BOLD+Green+"input"+Blink+" > "+RESET)

		if m2=='1':
			os.system('clear')
			
			crypt.john()

		if m2=='2':
			os.system('clear')
			
			crypt.hashcat()


	if m1=='3':
		os.system('clear')
		print(BOLD+Cyan+"------------- Payload Creation ------------\n"+RESET)
		print(BOLD+Cyan+"1.msfvenom \n"+RESET)
		print(BOLD+Cyan+"[+] Use Index Number As Input.\n"+RESET)
		mdf=input(BOLD+Green+"input"+Blink+" > "+RESET)

		if mdf=='1':
			os.system('clear')
			
			exploit.msfvenom()


	if m1=='4':
		os.system('clear')
		print(BOLD+Cyan+"------------- File Transfers ------------\n"+RESET)
		print(BOLD+Cyan+"1.HTTP Server \n2.FTP Server \n3.SMB Server\n"+RESET)
		print(BOLD+Cyan+"[+]Use Index Number As Input.\n"+RESET)
		m2=input(BOLD+Green+"input"+Blink+" > "+RESET)

		if m2=='1':
			os.system('clear')
			
			filetransfer.http()

		if m2=='2':
			os.system('clear')
			
			filetransfer.ftp()

		if m2=='3':
			os.system('clear')
			
			filetransfer.smb()



def exect(cmd):
	time.sleep(0.5)
	lg=input(BOLD+Blue+"[*] Would You Like To Execute This Command Right Now? Y/N : "+RESET)

	if lg=='Y' or lg=='y':
		print(BOLD+Green+"[+] Executing command..."+RESET)
		time.sleep(0.5)
		os.system(cmd)


	if lg=='N' or lg=='n':

		time.sleep(0.5)
		print(BOLD+Blue+"Bye :)")
		exit()

	else:
		time.sleep(0.5)
		exit()

def synt(fnc):
	print(BOLD+Green+'[+] Syntax used is : '+Yellow+fnc+RESET)
	

class recon:

	def nmap():
		
		print(BOLD+Cyan+"---------------------------------------------------"+RESET)
		print(BOLD+Cyan+"----------------------- nmap ----------------------"+RESET) 
		print(BOLD+Cyan+"---------------------------------------------------\n"+RESET)
		print(BOLD+Cyan+"1.Fast Scan \n2.All Ports Scan \n3.Detailed Scan \n")
		print(BOLD+Green+"[+] Select Type of Scan you want to perform.\n"+RESET)
		m2=input(BOLD+Green+"input"+Blink+" > "+RESET)
		os.system('clear')
		ip=input(BOLD+Green+"[*] Enter the IP Address you want to scan : "+RESET)
		
		if m2=='1':
			os.system('clear')
			nmapfst='nmap -F '+ip
			synt(nmapfst)
			print(BOLD+Green+'[+] here -F will Enable Fast Mode & Will Only Scan Top 100 Ports.')
			exect(nmapfst)

		if m2=='2':
			os.system('clear')
			nmapap='nmap -p- -vv '+ip
			synt(nmapap)
			print(BOLD+Green+'[+] here -p- flag will scan all 65,535 Ports.'+RESET)
			print(BOLD+Green+'[+] here -vv flag will show the ports as they get detected.'+RESET)
			exect(nmapap)

		if m2=='3':
			os.system('clear')
			nmapdet='nmap -p- -A -vv '+ip
			synt(nmapdet)
			print(BOLD+Green+'[+] here -p- flag will scan all 65,535 Ports.'+RESET)
			print(BOLD+Green+'[+] here -vv flag will show the ports as they get detected.'+RESET)
			print(BOLD+Green+'[+] here -A flag will enalbe detailed scan mode.'+RESET)
			exect(nmapdet)
		
		
		

	def gobuster():

		print(BOLD+Cyan+"---------------------------------------------------"+RESET)
		print(BOLD+Cyan+"--------------------- gobuster --------------------"+RESET) 
		print(BOLD+Cyan+"---------------------------------------------------\n"+RESET)
		url=" -u "+input(BOLD+Green+"[*] Enter the URL you want to use for directory busting : "+RESET)
		wordlist=" -w "+input(BOLD+Green+"[*] Enter the full path of the wordlist you want to use : "+RESET)
		os.system('clear')
		gobuster='gobuster dir'+url+wordlist+' -t 100'
		synt(gobuster)
		print(BOLD+Green+'[+] dir flag is mandatory for performing directory busting.'+RESET)
		print(BOLD+Green+'[+] -u flag is used to specify the URL of the website which is '+url+' in current scenario.'+RESET)
		print(BOLD+Green+'[+] -w flag is used to specify the wordlist you want to use which is '+wordlist+' in current scenario.'+RESET)
		print(BOLD+Green+'[+] -t flag is used to specify threads, more threads is more speed, consider it as a speed booster.'+RESET)
		exect(gobuster)


	def nikto():

		print(BOLD+Cyan+"---------------------------------------------------"+RESET)
		print(BOLD+Cyan+"----------------------- nikto ---------------------"+RESET) 
		print(BOLD+Cyan+"---------------------------------------------------\n"+RESET)
		host=" -h "+input(BOLD+Green+"[*] Enter the host you want to use for nikto scan : "+RESET)
		nikt='nikto '+host
		os.system('clear')
		synt(nikt)
		print(BOLD+Green+"[+] -h flag is used for specifying the host you want to scan in nikto."+RESET)
		exect(nikt)


class crypt:

	def john():

		print(BOLD+Cyan+"----------------------------------------------------------"+RESET)
		print(BOLD+Cyan+"--------------------- John The Ripper --------------------"+RESET) 
		print(BOLD+Cyan+"----------------------------------------------------------\n"+RESET)
		hast=input(BOLD+Green+"[+] Save Your Hash(es) on a file and please specify that file : "+RESET)
		formt=input(BOLD+Green+"[+] Please Specify Format of your hash(es) : "+RESET)
		wordlst=input(BOLD+Green+"[+] Please Specify The Wordlist you want to use : "+RESET)
		os.system('clear')	
		jtr='john '+hast+" --wordlist="+wordlst+" --format="+formt
		synt(jtr)
		print(BOLD+Green+"[+] --wordlist flag is used for specifying the wordlist you use for hash cracking."+RESET)
		print(BOLD+Green+"[+] --format flag is used for specifying the format of flag you want to crack."+RESET)			
		exect(jtr)


	def hashcat():

		print(BOLD+Cyan+"----------------------------------------------------------"+RESET)
		print(BOLD+Cyan+"------------------------- Hashcat ------------------------"+RESET) 
		print(BOLD+Cyan+"----------------------------------------------------------\n"+RESET)
		hsh=input(BOLD+Green+"[+] Save Your Hash(es) on a file and please specify that file : "+RESET)
		modul=input(BOLD+Green+"[+] Please Specify Module of your hash(es) : "+RESET)
		wordls=input(BOLD+Green+"[+] Please Specify The Wordlist you want to use : "+RESET)
		hsct='hashcat '+'-m '+modul+' '+hsh+' '+wordls
		os.system('clear')
		synt(hsct)
		print(BOLD+Green+"[+] -m flag will specify the module which is the hash type you want to crack.")
		exect(hsct)

		

class exploit:

	def msfvenom():
		print(BOLD+Cyan+"----------------------------------------------------------"+RESET)
		print(BOLD+Cyan+"------------------------ Msfvenom ------------------------"+RESET) 
		print(BOLD+Cyan+"----------------------------------------------------------\n"+RESET)
		pld=" -p "+input(BOLD+Green+"[*] Please Input The Payload You Want To Use : "+RESET)
		lhost=" LHOST="+input(BOLD+Green+"[*] Please Input Your LHOST : "+RESET)
		lport=" LPORT="+input(BOLD+Green+"[*] Please Input Your LPORT : "+RESET)
		frmt=input(BOLD+Green+"[*] Please Input Format of Your Payload : "+RESET)
		os.system('clear')
		vnm="msfvenom"+pld+lhost+lport+" -f "+frmt+" > payload"+"."+frmt
		synt(vnm)
		print(BOLD+Green+"[+] -p flag will specify the payload you want to use.")
		print(BOLD+Green+"[+] LHOST flag will specify the locahost address of your listener.")
		print(BOLD+Green+"[+] LPORT flag will specify the local port of your listener.")
		print(BOLD+Green+"[+] -f flag will specify the format of output payload.")
		exect(vnm)

		
				

class filetransfer:

	def http():
		print(BOLD+Cyan+"----------------------------------------------------------"+RESET)
		print(BOLD+Cyan+"---------------------- HTTP SERVER -----------------------"+RESET) 
		print(BOLD+Cyan+"----------------------------------------------------------\n"+RESET)
		prt=input(BOLD+Green+"[*] Enter the port number where you want to deploy the HTTP server : "+RESET)
		hserv='python3 -m http.server '+prt
		os.system('clear')
		synt(hserv)
		print(BOLD+Green+"[+] HTTP Server will be deployed on present working directory.")
		try:
			exect(hserv)
		except:
			print(Red+BOLD+"[-] HTTP Server Module is not installed!")
		


	def ftp():
		print(BOLD+Cyan+"----------------------------------------------------------"+RESET)
		print(BOLD+Cyan+"----------------------- FTP SERVER -----------------------"+RESET) 
		print(BOLD+Cyan+"----------------------------------------------------------\n"+RESET)
		prtt=' -p '+input(BOLD+Green+"[*] Enter the port number where you want to deploy the FTP server : "+RESET)
		fserv='python3 -m pyftpdlib '+prtt
		os.system('clear')
		synt(fserv)
		print(BOLD+Green+"[+] FTP Server will be deployed on present working directory.")
		try:
			exect(fserv)
		except:
			print(Red+BOLD+"[-] FTP Server Module is not installed! (Install using pip install pyftpdlib)")


	def smb():
		print(BOLD+Cyan+"----------------------------------------------------------"+RESET)
		print(BOLD+Cyan+"---------------------SMB SERVER -----------------------"+RESET) 
		print(BOLD+Cyan+"----------------------------------------------------------\n"+RESET)
		sserv='impacket-smbserver share .'
		os.system('clear')
		synt(sserv)
		print(BOLD+Green+"[+] SMB Server will be deployed on present working directory."+RESET)
		try:
			exect(sserv)
		except:
			print(Red+BOLD+"[-] Impakcet is not installed!")


#class resouces:

#	def resources()




if __name__ == "__main__":

	logo()
	toolcheck()
	mainmenu()
