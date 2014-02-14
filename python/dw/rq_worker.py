import sys
import requests

urls = [ x for x in sys.stdin ]

for url in urls:
    r = requests.get( url.rstrip() )
    print(r.status_code)

