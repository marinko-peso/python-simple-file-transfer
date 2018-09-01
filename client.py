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
destionation_file = config['DEFAULT']['DestinationFile']

# Ask for host details and open a connection.
s = socket.socket()
host = input(str('Enter the \033[94mhost\033[0m address of the server: '))
s.connect((host, port))
print('Connected to host...')

# Ask for received file name, if not specified use settings.
filename = input(str('Enter the name for the incoming file (if left empty, settings will be used): '))
if not filename:
    filename = destionation_file

# Create and receive the file.
file = open(filename, 'wb')
file_data = s.recv(1024)
file.write(file_data)
file.close()
print('File has been received.')
