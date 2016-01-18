import platform
import sys

import browser
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



    script, ip, port, action = sys.argv
    if action == "--help":
        print(help_string)
    elif action == '--listen':
        server.listen(ip, port)
    elif action == '--send':
        system_os = platform.system()
        links = browser.retrieve_next_session_links(system_os)
        client.send(links, ip , port)

main()
