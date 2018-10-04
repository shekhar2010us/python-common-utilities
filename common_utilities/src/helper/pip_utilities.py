import json
import urllib.request
from distutils.version import StrictVersion
import pip


class PipUtilities:

    def __init__(self):
        self.class_name = self.__class__.__name__

    def package_version(self, package_name) -> list:
        url = "https://pypi.python.org/pypi/%s/json" % (package_name,)
        data = json.load(urllib.request.urlopen(url))
        versions = data["releases"].keys()
        return list(versions)

    def package_install(self, package):
        if hasattr(pip, 'main'):
            pip.main(['install', package])
        # else:
        #     pip._internal.main(['install', package])
