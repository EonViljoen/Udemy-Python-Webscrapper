# from bs4 import BeautifulSoup
import requests
from lxml import html

# # Search
# search = input("Enter Search Term:")
# params = {"q": search}
# link = "https://www.bing.com/search?q=pizza"
# r = requests.get(link)
#
# soup = BeautifulSoup(r.content, "html.parser")
# # Find Results with id being b_results
# results = soup.find("ol", {"id": "b_results"})
# links = results.findAll("li", {"class": "b_algo"})
# # doesn't print out now
# # print(r.text)
# # print(results)
# # print(links)
#
# for item in links:
#     item_text = item.find("a").text
#     item_href = item.find("a").attrs["href"]
#
#     if item_text and item_href:
#         print(item_text)
#         print(item_href)
#
# print(results)

URL = "https://www.google.com/search?&q=python+sessions+is+not+callable"
session_requests = requests.session()
result = session_requests.get(URL, headers = dict(referer = URL))
tree = html.fromstring(result.content)
units = tree.xpath('//text()')
print(units)
