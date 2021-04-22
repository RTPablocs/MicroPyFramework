from pyfiglet import Figlet
import urllib.parse as parser

def bannerGenerator():
    f = Figlet(font='slant')
    return f.renderText('MicroPyFW')

def urlParse(url):
    result = parser.urlparse(url)
    return result.path