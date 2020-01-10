def play_radio(station, stop_t):
    import urllib
    import urllib.request
    import requests
    import discord as dc
    import os
    import sys
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
        "LALEGUL" : 'http://live46.netmedya.net:443/lalegulfm?/'
    }

    r = requests.get(STATIONS[station], stream=True)
    with open('stream.mp3', 'wb') as f:
        for block in r.iter_content(1024):
            f.write(block)
            print(stop_t())
            if stop_t():
                sys.stdout.flush()
                r.close()
                f.close()
                os.remove("stream.mp3") 