import urllib.request


class UrlUtilities:

    def __init__(self):
        self.class_name = self.class_name = self.__class__.__name__

    def read_url(self, url) -> str:
        fp = urllib.request.urlopen(url)
        out_bytes = fp.read()
        out = out_bytes.decode("utf8")
        fp.close()
        return out
