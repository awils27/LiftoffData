import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 9001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Open the file to read the saved UDP messages
with open("liftoff.bin", "rb") as file:  # Use "rb" mode to read binary data
    for line in file:
        # Send each line/message over UDP
        sock.sendto(line.rstrip(b"\n"), (UDP_IP, UDP_PORT))