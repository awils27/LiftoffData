import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 9001


sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))


last_message = b""  # Variable to store the last received message

print('Writing to file')

with open("liftoff.bin", "ab") as file:  # Use "ab" mode to write binary data
    while True:
        udp_message, addr = sock.recvfrom(1024)

        #Check if the received message is different from the last one
        if udp_message != last_message:
            # Write the binary message to the file
            file.write(udp_message + b"\n")  # Add a newline character after each message
            last_message = udp_message  # Update the last received message