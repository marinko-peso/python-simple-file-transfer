import socket
import configparser
import sys


# Read config settings.
config = configparser.ConfigParser()
config.read('config.ini')
if not 'Port' in config['DEFAULT']:
    print('Config is corrupted. Exiting...')
    sys.exit(0)

# Extract settings.
port = int(config['DEFAULT']['Port'])
source_file = config['DEFAULT']['SourceFile']

# Open socket and listen for incoming connections.
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(1)
print(host)
print('Waiting for connections...')

# Accept incoming connection.
connection, address = s.accept()
print(address, 'Has connected.')

# Get file to send. If none is specified from user, use source_file from config.
filename = input(str('Enter the filename (if left empty, settings will be used): '))
if not filename:
    filename = source_file

# Send file content.
file = open(filename, 'rb')
file_data = file.read(1024)
connection.send(file_data)
print('Data has been transmitted.')
