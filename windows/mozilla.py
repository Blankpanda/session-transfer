import subprocess
import sys

script , input_file = sys.argv

if input_file not "links.txt":
    print("Invalid input.  Use session-transfer/links.txt, " +
    "after you haver recieved the links ")
else:
    f = open(input_file, 'a')
    links = f.read()
    path = "C:\\Program_Files(x86)\\Mozilla_Firefox\\firefox.exe"
    links = [path] + links
    subprocess.call([links])
