from scrapling.fetchers import Fetcher

Fetcher.adaptive = True
Fetcher.keep_comments = False
Fetcher.keep_cdata = False
# fetch the webpage
page = Fetcher.get("https://www.chollometro.com/")

# extract raw HTML
print(page.html_content)
