import socket

port = 8080

s = socket.socket()
host = input(str('Enter the host address of the server: '))
s.connect((host, port))
print('Connected to host...')

filename = input(str('Enter the name for the incoming file: '))
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print('File has been received.')
