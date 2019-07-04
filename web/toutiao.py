from selenium import webdriver
from lxml import etree
import time

def gethtml(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(3)
    for x in range(400):
        js = "var q=document.documentElement.scrollTop=" + str(x * 1000)
        driver.execute_script(js)
        time.sleep(1)
    html = driver.page_source
    html=etree.HTML(html)
    return html

def gettitle(Html):
    titles=Html.xpath('//div[@class="wcommonFeed"]/ul/li/div/div[1]/div/div[1]/a/text()')
    print(len(titles))
    return titles
def writetitle(titles,filename):
    with open(filename,'w',encoding='utf-8') as file:
        for title in titles:
            file.write(title+'\n')
    return


def main():
    labels=[
        'news_tech',
        'news_entertainment',
        'news_game',
        'news_sports',
        'news_car',
    ]

    for label in labels:
        url = 'https://landing.toutiao.com/ch/%s/'%label
        html = gethtml(url)
        titles = gettitle(html)
        writetitle(titles,'news/%s.txt'%label)

if __name__ == '__main__':
    main()





