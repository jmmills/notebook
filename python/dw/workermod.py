import requests

class Foo:
    def count_words_at_url(self,url):
        r = requests.get(url)
        return len(r.text.split())

