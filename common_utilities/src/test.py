import sys
sys.path.append("../")

from helper.general import url_utilities
from helper import pip_utilities

pip_obj = pip_utilities.PipUtilities()
url_obj = url_utilities.UrlUtilities()

# Test pip version
def test_pip_version(package):
    print(pip_obj.package_version(package))
    print(type(pip_obj.package_version(package)))

# Test pip install
def test_pip_install(package):
    print(pip_obj.package_version(package))
    print(type(pip_obj.package_version(package)))
    pip_obj.package_install(package)

# Test url utils
def test_read_url(url):
    out = url_obj.read_url(url)
    print(out[1000:1010])


def main():
    p1 = "Theano"
    test_pip_version(p1)

    p2 = "pytest"
    test_pip_install(p2)

    url = "https://clinicaltrials.gov/ct2/show/NCT03254875?cond=Cancer&rank=1"
    test_read_url(url)


if __name__ == '__main__':
    main()