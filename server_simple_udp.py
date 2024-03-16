# Ayub Yusuf
# pw2712gz
# Assignment 2 

import socket
import sys
import datetime
import hashlib

# Function to compute MD5 checksum of the given data
def compute_checksum(data):
    return hashlib.md5(data).hexdigest()

# Main function to listen for messages from clients
def main(port):
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Bind the socket to listen on the specified port
    server_socket.bind(('', int(port)))

    print(f"Listening on port {port}\n")

    while True:
        print("Waiting ...\n")
        # Receive data from a client
        data, address = server_socket.recvfrom(4096)
        
        # Split the received data into checksum and message
        checksum, message = data.split(b"|", 1)
        received_checksum = checksum.decode()
        # Compute the checksum of the received message
        calculated_checksum = compute_checksum(message)
        
        print("*** new message ***\n")
        print(f"Received time: {datetime.datetime.now()}")
        print(f"Received message: \n{message.decode()}")
        print(f"Received checksum: {received_checksum}")
        print(f"Calculated checksum: {calculated_checksum}\n")
        
        # Compare the received checksum with the calculated checksum
        if received_checksum == calculated_checksum:
            # If they match, send back the current timestamp
            response = str(datetime.datetime.now()).encode()
        else:
            # If they do not match, send an error message
            response = b'0'
            print("Error: Checksum does not match\n")
            
        # Send the response to the client
        server_socket.sendto(response, address)

# Entry point of the script
if __name__ == "__main__":
    # Ensure proper usage
    if len(sys.argv) != 2:
        print("Usage: python3 server_simple_udp.py <port_num>")
        sys.exit(1)
    # Call main function with command line argument
    main(sys.argv[1])
