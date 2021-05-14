from pyfiglet import Figlet
import urllib.parse as parser


def banner_generate():
    f = Figlet(font='slant')
    return f.renderText('MicroPyFW')


def url_parse(url):
    result = parser.urlparse(url)
    return result.path
