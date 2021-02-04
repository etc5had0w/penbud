# penbud - Penetration Tester Buddy

PENBUD is penetration testing buddy which helps you in penetration testing by making various important tools interactive.

I have created this tool mainly for newcomers but everyone can use it.

This tool has implemented Intractive version of famous command line tools.

If you dont like using flags or if you are confused using these tools then penbud is made for you.

This tool will run these tools by asking the parameters and it will print the finl syntax.

Now either you can copy the syntax and use it or you can execute the syntax right from the penbud tool itself.

The will will also give you explaination of various flags used in the final syntax making it easier to learn.

## How To Install :  

```
git clone https://github.com/etc5had0w/penbud.git
cd penbud/
ln -s ${PWD}/penbud.py /usr/bin/penbud
```
## How To Use :

run this commands from your terminal:

```
penbud
```


![demo](https://github.com/etc5had0w/penbud/blob/main/demo.png?raw=true "Title")



Right now the tools is integrating following tools :

nmap

gobuster

nikto

john

hashcat

msfvenom


The tool will also help in starting file transfer servers , curruntly supporting :

http server

ftp server

smb server
