import requests
import re
from bs4 import BeautifulSoup

URL = "https://www.johnlewis.com/2018-apple-ipad-pro-12-9-inch-a12x-bionic-ios-wi-fi-cellular-64gb/p3834601"
TAG_NAME = "span"
QUERY = {"class":"price__current"}

response = requests.get(URL)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
element = soup.find(TAG_NAME, QUERY)
string_price = element.text.strip()

pattern = re.compile(r"(\d+,?\d+.\d\d)")
match = pattern.search(string_price)
found_price = match.group(1)
without_commas = found_price.replace(",", "")
price = float(without_commas)

print(price)