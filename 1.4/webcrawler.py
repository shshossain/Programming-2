""" 
This is a crawler program using beautifulsoup.
It crawls the website "https://sport050.nl/sportaanbieders/alle-aanbieders/"
and fetches all the sport suppliers in the city of Groningen. It outputs 
a csv-file with the url;phone-number;email-address of all the suppliers it can find.
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

class Crawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.pointer = 0
        self.sub_urls = []
    
 
    def hack_ssl():
        """ ignores the certificate errors"""
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        return ctx

    def open_url(self, url):
        """ reads url file as a big string and cleans the html file to make it
        more readable. input: url, output: soup object
        """
        ctx = self.hack_ssl()
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def read_hrefs(self, soup):
        """ get from soup object a list of anchor tags,
        get the href keys and and prints them. Input: soup object
        """
        reflist = []
        tags = soup('a')
        for tag in tags:
            reflist.append(tag)
        return reflist

    def read_li(self, soup):
        lilist = []
        tags = soup('li')
        for tag in tags:
            lilist.append(tag)
        return lilist

    def get_phone(self, info):
        reg = r"(?:(?:00|\+)?[0-9]{4})?(?:[ .-][0-9]{3}){1,5}"
        phone = [s for s in info if 'Telefoon' in str(s)]
        try:
            phone = str(phone[0])
        except:
            phone = [s for s in info if re.findall(reg, str(s))]
            try:
                phone = str(phone[0])
            except:
                phone = ""   
        return phone.replace('Facebook', '').replace('Telefoon:', '')

    def get_email(self, soup):
        try: 
            email = [s for s in soup if '@' in str(s)]
            email = str(email[0])[4:-5]
            bs = BeautifulSoup(email, features="html.parser")
            email = bs.find('a').attrs['href'].replace('mailto:', '')
        except:
            email = ""
        return email


    def remove_html_tags(text):
        """Remove HTML tags from a string"""
        clean = re.compile('<.*?>')
        return re.sub(clean, '', text)

    def fetch_sidebar(self, soup):
        """ reads html file as a big string and cleans the html file to make it
        more readable. input: html, output: tables
        """
        sidebar = soup.find_all(attrs={'class': 'sidebar'})
        return sidebar[0]


    def extract(url):
        text = str(url)
        text = text[26:].split('"')[0] + "/"
        return text

    def initialize_sub_urls(self):
        print('fetch urls')
        url = self.base_url
        s = self.open_url(url)
        reflist = self.read_hrefs(s)
        print('getting sub-urls')
        self.sub_urls = [s for s in reflist if '<a href="/sportaanbieders' in str(s)]
        self.sub_urls = self.sub_urls[3:]
        print(f'{len(self.sub_urls)} sub-urls')

    def __iter__(self):
        if not self.sub_urls:
            self.initialize_sub_urls()
        return self

    def __next__(self):
        if self.pointer >= len(self.sub_urls):
            raise StopIteration
        
        sub = self.sub_urls[self.pointer]
        self.pointer += 1 #Move to next sub-URL
        
        try:
            sub = self.extract(sub)
            site = self.base_url[:-16] + sub
            soup = self.open_url(site)    
            info = self.fetch_sidebar(soup)
            info = self.read_li(info)
            phone = self.get_phone(info)
            phone = self.remove_html_tags(phone).strip()
            email = self.get_email(info)
            email = self.remove_html_tags(email).replace("/", "")
            return f'{site} ; {phone} ; {email}'
        except Exception as e:
            print(e)
            return None
