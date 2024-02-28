import socket
import struct

UDP_IP = "127.0.0.1"
UDP_PORT = 9001


sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    offset = 0
    udp_message, addr = sock.recvfrom(1024)

    for fmt in format_strings:
        size = struct.calcsize(fmt)
        value = struct.unpack(fmt, udp_message[offset:offset+size])
        data.append(value)
        offset += size

    num_motors = struct.unpack('<B', udp_message[offset:offset+1])[0]
    offset += 1
    motor_rpm = []
    for _ in range(num_motors):
        motor_rpm.append(struct.unpack('f', udp_message[offset:offset+4])[0])
        offset += 4
    
    print("Timestamp:", data[0][0])
    print("Position:", data[1])
    print("Attitude:", data[2])
    print("Gyro:", data[3])
    print("Input:", data[4])
    print("Battery:", data[5])
    print("Motor RPM:", motor_rpm)
