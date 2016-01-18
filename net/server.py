# accepts a message from a client this information will be read with a bash script

import socket

def listen(UDP_IP, UDP_PORT):

    # make sure UDP_PORT is an int
    UDP_PORT = int(UDP_PORT)

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to ip and port
    serversocket.bind((UDP_IP, UDP_PORT))
    serversocket.listen(1) # sure why not 1


    conn, addr = serversocket.accept()

    #accept a connection
    data = conn.recv(4096)
    print("Data recieved.")

    # write the data to a text file
    f = open("links.txt", 'a')
    print("Writing Data.")

    # we want the file to have no quotations, with a one line spaced out
    # hyperlinks
    data = str(data)
    data = data.replace("'", '')
    data = data.replace('"', '')
    # python signifes byte types like b"string", we want to remove the b
    # since were saving it in plaintext
    data = data.replace('b' , '')

    # converts the data into a list and writes it
    data = data.split('|')

    for link in data: f.write(link + '\n')

    f.close()


    print("data located in links.txt")
    #con.close()
