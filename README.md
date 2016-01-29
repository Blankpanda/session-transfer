# session-transfer
session-transfer is the tool that I use to transfer my mozillas browser session from my desktop computer to my laptop.

Currently the only options available are the following:

transfering from Mozilla on Windows to Linux:

  On your Linux Machine type the following:
      ```
          python main.py <IP address of your linux machine> <portnumber> --listen
      ```
  On your Windows Machine type the following:
      ```
          python main.py <IP address of your linux machine> <portnumber> --send
      ```
  And Finally on your Linux Machine type the following:
      ```
          ./linux/<browser>.sh links.txt
      ```
