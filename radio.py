import urllib
import urllib.request
import requests
import discord as dc
import os
import sys
import bs4
import datetime

def play_radio(station, stop_t):
    def NiceToICY(self):
        class InterceptedHTTPResponse():
            pass
        import io
        line = self.fp.readline().replace(b"ICY 200 OK\r\n", b"HTTP/1.0 200 OK\r\n")
        InterceptedSelf = InterceptedHTTPResponse()
        InterceptedSelf.fp = io.BufferedReader(io.BytesIO(line))
        InterceptedSelf.debuglevel = self.debuglevel
        InterceptedSelf._close_conn = self._close_conn
        return ORIGINAL_HTTP_CLIENT_READ_STATUS(InterceptedSelf)

    ORIGINAL_HTTP_CLIENT_READ_STATUS = urllib.request.http.client.HTTPResponse._read_status
    urllib.request.http.client.HTTPResponse._read_status = NiceToICY

    STATIONS = {
        "PAL_FM" : 'http://shoutcast.radyogrup.com:1030/',
        "LALEGUL" : 'http://live46.netmedya.net:443/lalegulfm?/',
        "ROCK" : "http://stream.rockfm.com.tr:9450/;"
    }

    print("RUNNINGG")
    r = requests.get(STATIONS[station], stream=True)
    with open('stream.mp3', 'wb') as f:
        for block in r.iter_content(1024):
            f.write(block)
            if stop_t():
                sys.stdout.flush()
                r.close()
                f.close()
                os.remove("stream.mp3")

def get_cuma_saati():
    URL = "https://namazvakitleri.diyanet.gov.tr/tr-TR/9541/istanbul-icin-namaz-vakti"
    headers = {
        "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:69.0) Gecko/20100101 Firefox/69.0"
    }

    page = requests.get(URL, headers=headers)
    soup = bs4.BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table')
    haftalik  = []

    for row in table.findAll('tr')[1:250]:
        col = row.findAll('td')
        saat = col[3].getText()
        haftalik.append(saat)

    cuma = haftalik[4]
    return cuma.split(':')












