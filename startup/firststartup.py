import urllib.request
from bs4 import BeautifulSoup
import os
import re
import subprocess
from subprocess import STDOUT,PIPE

forgeversion = os.getenv('FORGEVERSION', 'latest')
mc_version = os.getenv("MC_VERSION")
download_url = "https://files.minecraftforge.net/net/minecraftforge/forge/index_" + mc_version + ".html"

if not os.path.isfile("already_started"):
    f = open("already_started", "a")
    f.close()
    fpreq = urllib.request.Request(download_url, headers={'User-Agent': 'Mozilla/5.0'})
    fp = urllib.request.urlopen(fpreq)
    mybytes = fp.read()
    html = mybytes.decode("utf8")
    fp.close()
    soup = BeautifulSoup(html, 'html.parser')
    downloads = soup.body.find_all('div', attrs={'class':'download'})
    if forgeversion == 'latest':
        url = downloads[0].a['href']
    else:
        url = downloads[1].a['href']
    
    finalurl = re.sub('(https:\/\/adfoc\.us\/serve\/sitelinks\/+[-?]+id=[\d]+&url=)', '', url)
    opener = urllib.request.URLopener()
    opener.addheader('User-Agent', 'Mozilla/5.0')
    filename, headers = opener.retrieve(finalurl, 'forge.jar')
    #urlrequest = urllib.request.urlretrieve(finalurl, "forge.jar")
    proc = subprocess.run(['java', '-jar', 'forge.jar', '--installServer', '.'])
    
    if os.path.isfile("forge.jar"):
        os.remove("forge.jar")
