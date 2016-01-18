#
# retrieves information from mozilla firefox browsers settings based off of
# platform.  the information being retrieved is tabs that will be opened
# on the next session
#

import os

#
#  get the list of links that are opened on startup
#  since the lists are seperated by a | delimiter, we
#  seperate them into a list
#
def retrieve_next_session_links(system):

    # get the paths for the firefox settings
    if system == 'Windows':

        path = os.environ['APPDATA'] # C:\\<user>\\AppData\\Roaming
        path += "\\Mozilla\\Firefox\\Profiles\\"
        profile = get_profile(path) # k9kvq567.default
        path += profile + "\\prefs.js"

    elif system == 'Linux':

        path = "~/.mozilla/prefs.js"

    # open the prefs.js file and look for the line like:
    #       user_pref("browser.startup.homepage", "...")
    key = """user_pref("browser.startup.homepage", """
    raw_links = str()

    # opens prefs.js and reads for the key
    prefs = open(path)
    for line in prefs:
        if key in line:
            raw_links = line
            break


    raw_links = raw_links[len(key):].strip() # get rid of the first half that
                                             # doesnt contain the hyperlinks

    # seperate the the string into a list using the | delimiter
    links = raw_links.split("|")

    # remove any entry in the list isnt a http or http address
    for link in links:
        if "http" not in link: # covers https as well.
            links.remove(link)

    return links


#
# return the name of default profile
# for directories in os.listdir()
#
def get_profile(path):

    for directory in os.listdir(path):
        if "default" in directory:
            return directory
