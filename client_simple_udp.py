# Ayub Yusuf
# pw2712gz
# Assignment 2 

import socket
import sys
import time
import hashlib


# Function to compute MD5 checksum of the given data
def compute_checksum(data):
    return hashlib.md5(data).hexdigest()


# Main function to send a message or file to the server
def main(server_ip, port, data_input):
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = (server_ip, int(port))

    # If the third argument is a file or a message
    try:
        # Attempt to open and read the file
        with open(data_input, 'rb') as file:
            data = file.read()
    except FileNotFoundError:
        # If the file is not found, treat the input as a message
        data = data_input.encode()

    # Compute the checksum of the data
    checksum = compute_checksum(data)
    # Combine the checksum and the data into one message
    message = checksum.encode() + b"|" + data

    # Record the start time
    start_time = time.time()
    # Send the combined message to the server
    client_socket.sendto(message, address)

    # Wait for a response from the server
    response, _ = client_socket.recvfrom(4096)
    # Record the end time when the response is received
    end_time = time.time()

    # Calculate the round-trip time in microseconds
    rtt = (end_time - start_time) * 1000000

    print(f"checksum sent: {checksum}")

    # Check if the response is an error message
    if response.decode() == '0':
        print("message failed!")
    else:
        print(f"server has successfully received the message at {response.decode()}")
    print(f"RTT: {int(rtt)}us")

    client_socket.close()


# Entry point of the script
if __name__ == "__main__":
    # Ensure proper usage
    if len(sys.argv) != 4:
        print("Usage: python3 client_simple_udp.py <server_ip> <port_num> <'Test text'|test_file.txt>")
        sys.exit(1)
    # Call main function with command line arguments
    main(sys.argv[1], sys.argv[2], sys.argv[3])
