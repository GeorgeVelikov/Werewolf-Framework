import socket;

IP = socket.gethostbyname(socket.gethostname());
PORT = 26011;
ADDRESS = (IP, PORT);

BYTE = 2**10;
KILOBYTE = 2**20;

DATETIME_FORMAT = "%m/%d/%Y, %H:%M:%S"