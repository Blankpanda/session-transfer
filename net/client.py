#
# sends appended text information to a "server"
# thats is listening.
#

import socket

def send(information, UDP_IP, UDP_PORT):

    # make sure UDP_PORT is an int
    UDP_PORT = int(UDP_PORT)
    information = append_list(information) # prepare the data to send
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((UDP_IP, UDP_PORT))
    client_socket.send(bytes(information, 'utf-8'))

    data = client_socket.recv(4096)


# appends a list into string with | delimiter
def append_list(list):

    appended_list = ""

    for item in list:
        appended_list += item + '|'

    return appended_list.strip()
