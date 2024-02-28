import socket
import gzip

UDP_IP = "127.0.0.1"
UDP_PORT = 9001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Open the file to read the saved UDP messages
    with open("udp_messages.bin", "rb") as file:  # Use "rb" mode to read binary data
        while True:
            # Read each line/message from the file
            for line in file:
                # Send each line/message over UDP
                sock.sendto(line.rstrip(b"\n"), (UDP_IP, UDP_PORT))
            
            # Once end of file is reached, go back to the beginning
            file.seek(0)