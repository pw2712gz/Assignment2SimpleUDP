# Simple UDP Client-Server Application

This application consists of a UDP server and client that demonstrate basic network communication in Python. The client sends a message or the contents of a file to the server, which responds with the timestamp of when the message was received. The client then calculates and displays the round-trip time (RTT).

## Files in the Directory

- `client_simple_udp.py`: The client program. It sends messages or file contents to the server.
- `server_simple_udp.py`: The server program. It listens for messages from the client and responds with timestamps.
- `README.md`: This file.

## Instructions

### Running the Server

1. Open a terminal.
2. Navigate to the directory containing the server script.
3. Run the server using the following command:
   ```
   python3 server_simple_udp.py <port_num>
   ```
   Replace `<port_num>` with the port number you want the server to listen on.

### Running the Client

1. Open a terminal (can be on the same machine as the server or a different one).
2. Navigate to the directory containing the client script.
3. Run the client using one of the following commands:
   - To send a text message:
     ```
     python3 client_simple_udp.py <server_ip> <port_num> "<message>"
     ```
     Replace `<server_ip>` with the server's IP address, `<port_num>` with the port number, and `<message>` with the message you want to send.
   - To send a file:
     ```
     python3 client_simple_udp.py <server_ip> <port_num> <file_path>
     ```
     Replace `<file_path>` with the path to the file you want to send.

## Example

To send the text "Hello, World!" to a server running on the same machine (localhost) using port 4123:

```
python3 client_simple_udp.py 127.0.0.1 4123 "Hello, World!"
```

To send the contents of `sample.txt` to a server with IP address `192.168.1.2` using port 4123:

```
python3 client_simple_udp.py 192.168.1.2 4123 sample.txt
```

