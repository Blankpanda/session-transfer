import platform
import sys

import browser
from net import client, server
import net


def main():

    help_string = """
    usage: python main.py <IP_ADDR> <PORT> <ACTION>

    IP_ADDR :   IP address of the server/client
    PORT :      Port number of the server/client
    Action :    specifies wether you want to send or listen

    Actions:
                --listen (listens for a connection the specifed port)
                --send   (sends appended string from mozilla settings)
     """


    try:
        script, ip, port, action = sys.argv
    except Exception as e:
        print(help_string)
        

    if action == "--help":
        print(help_string)
    elif action == '--listen':
        server.listen(ip, port)
    elif action == '--send':
        system_os = platform.system()
        links = browser.retrieve_next_session_links(system_os)
        client.send(links, ip , port)

main()
