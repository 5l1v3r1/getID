#!/usr/bin/python
# Get FB Profile,Page,Group{ID}
# By: Oseid Aldary
#
import requests,re,sys,socket

def cnet():
    try:
        ip = socket.gethostbyname("www.google.com")
        con = socket.create_connection((ip, 80), 2)
        return True
    except socket.error:
        pass
    return False

def ID(url):
    if cnet() !=True:
        print("\n[!] Error: Please Check Your Internet Connection !!!")
        exit(1)
    try:
        idre = re.compile('"entity_id":"([0-9]+)"')
        con = requests.get(url).content
        idis = idre.findall(con)
        print("\n[*] ID: "+idis[0])
    except IndexError:
        print("\n[!] Error: 404 Not Found !!!")
        exit(1)
if len(sys.argv) !=2:
    print("\nUsage: python getid.py <profile_link OR Page_link>\n\nExamples:\n      [Profile~ID] python getid.py https://www.facebook.com/alanwalker97\n      [Group~ID] python getid.py https://www.facebook.com/groups/madrassatechfamily/\n      [Page-ID] python getid.py https://www.facebook.com/MadrasaTech/")
    exit(1)
url = sys.argv[1]
ID(url)

#--- End Of File ---#

