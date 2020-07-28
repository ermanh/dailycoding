'''
2020-07-29
[from dailycodingproblem.com #55]

Implement a URL shortener with the following methods:

shorten(url)
    - shortens the url into a six-character alphanumeric string (e.g. zLg6wl)
restore(short)
    - expands the shortened string into the original url
    - if no such shortened string exists, return null

Hint: What if we enter the same URL twice?
'''

from random import randint


class URLShortener:

    def __init__(self):
        self.SHORT_LENGTH = 6
        self.CHARS = 'abcdefghijklmnopqrstuvqxyz' + \
                     'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + '0123456789'
        self.dictionary = {}
        self.inverted = {}
            # Another option is to create the inverted dictionary only on
            # demand (in place of the first two lines of shorten(self, url)), 
            # but that trades memory for slower processing speed

    def _random_char(self):
        return self.CHARS[randint(0, len(self.CHARS) -1)]

    def _gen_code(self):
        return ''.join(self._random_char() for _ in range(self.SHORT_LENGTH))

    def shorten(self, url):
        if url in self.inverted:
            return self.inverted.get(url)

        code = self._gen_code()
        while code in self.dictionary:  # in case of code duplication
            code = self._gen_code()
        
        self.dictionary[code] = url
        self.inverted[url] = code
        return code
        
    def restore(self, short):
        return self.dictionary.get(short)


'''
# TESTS

url1 = 'https://github.com'
url2 = 'https://shortening.co'
url3 = 'https://coffee.com'

us = URLShortener()
code1 = us.shorten(url1) 
code2 = us.shorten(url2)
print(code1, code2)

us.shorten(url1) == code1
us.restore(code1) == url1

us.restore(code2) == url2
us.shorten(url2) == code2

non_short = 'l3khG4'
while non_short in us.dictionary:
    non_short = us._gen_code()
us.restore(non_short) is None
'''
