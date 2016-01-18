# accepts a message from a client this information will be read with a bash script

import socket

def listen(UDP_IP, UDP_PORT):

    # make sure UDP_PORT is an int
    UDP_PORT = int(UDP_PORT)

    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to ip and port
    serversocket.bind((UDP_IP, UDP_PORT))
    serversocket.listen(1) # sure why not 1

    data = ""
    conn, addr = serversocket.accept()
    while 1:
        #accept a connection
        data = conn.recv(4096)

        # write the data to a text file
        f = open("links.txt")
        f.write(data)
        f.close()
        
        if data != "": conn.close() # close out if weve retrieved data

    con.close()
