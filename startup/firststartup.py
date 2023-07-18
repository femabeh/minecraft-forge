import urllib.request
from bs4 import BeautifulSoup
import os
import re
import requests
import subprocess
from subprocess import STDOUT,PIPE

if not os.path.isfile("already_started"):
    f = open("already_started", "a")
    f.close()
    fp = urllib.request.urlopen("https://files.minecraftforge.net/net/minecraftforge/forge/")
    mybytes = fp.read()
    html = mybytes.decode("utf8")
    fp.close()
    soup = BeautifulSoup(html, 'html.parser')
    forgeversion = os.getenv('FORGEVERSION', 'latest')
    downloads = soup.body.find_all('div', attrs={'class':'download'})
    if forgeversion == 'latest':
        url = downloads[0].a['href']
    else:
        url = downloads[1].a['href']
    
    finalurl = re.sub('(https:\/\/adfoc\.us\/serve\/sitelinks\/+[-?]+id=[\d]+&url=)', '', url)
    urlrequest = urllib.request.urlretrieve(finalurl, "forge.jar")
    proc = subprocess.run(['java', '-jar', 'forge.jar', '--installServer', '.'])
    
    if os.path.isfile("forge.jar"):
        os.remove("forge.jar")