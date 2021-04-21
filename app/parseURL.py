import urllib.parse as parser
import re


def urlParse(url):
    result = parser.urlparse(url)
    return result.path