from selenium import webdriver
ZHIHU_ANSWEROR_PAGE = "https://www.zhihu.com/org/datafuntalk" 
CLOSE_XPATH = "/html/body/div[4]/div/div/div/div[2]/button"
CHROMEDRIVER_PATH = "/Users/xiuminke/Downloads/chromedriver"
SCROLL_TIMES = 100 ## how many times the scroll action will be done. 

browser=webdriver.Chrome(CHROMEDRIVER_PATH) ## initiate a browser.
browser.get(ZHIHU_ANSWEROR_PAGE) ## get the page.
browser.find_element_by_xpath(CLOSE_XPATH).click() ## close the log_in page.

import time
for i in range(SCROLL_TIMES):
    ## scroll to the end.
    time.sleep(0.1)
    browser.execute_script("document.documentElement.scrollTop=100000000") 

from lxml import etree
html = etree.HTML(browser.page_source)

pages = html.xpath("//div[@class='ContentItem ArticleItem']") ## parse the html.

## get the headlines and urls ready. 
headlines = pages[0].xpath("//meta[@itemprop='headline']/@content")
urls = [url for url in pages[0].xpath("//meta[@itemprop='url']/@content") if "http" not in url]

with open("file.md", "w", encoding="utf-8") as f: 
    ## print the headlines and urls to a file. 
    for headline, url in zip(headlines, urls):
        f.write(f"- [ ] [{headline}](https:{url})\n")

browser.close() ## close the browser. 
