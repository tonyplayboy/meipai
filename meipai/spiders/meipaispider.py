import scrapy
import uuid
import time
from scrapy.spiders import CrawlSpider, Rule, Spider
from meipai.items import MeipaiItem
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class MeipaiSpider(Spider):
    name = 'meipai'
    allowed_domains = ['www.meipai.com', 'mvvideo10.meitudata.com', 'mvvideo11.meitudata.com', ]
    # url = 'http://www.tu11.com/xingganmeinvxiezhen/list_1_'
    # offset = 1
    start_urls = ['http://www.meipai.com/medias/hot', ]

    def parse(self, response):
        items = response.xpath('//ul[@id="mediasList"]/li/div/a[@class="content-l-p pa"]')
        item_list = items[:1]
        for i in item_list:

            video_link = i.xpath('.//@href').extract()[0]
            # http: // www.meipai.com / media / 1039574971
            yield scrapy.Request('http://www.meipai.com' + video_link, callback=self.content)


        # next_page = response.xpath('//dl[@class="list-left public-box"]/dd[@class="page"]//a[last()-1]/text()')
        # if "下一页" == next_page.extract()[0]:
        # next_page_url = response.xpath('//dl[@class="list-left public-box"]/dd[@class="page"]//a[last()-1]/@href').extract()[0]
        #     yield response.follow(next_page_url, callback=self.parse)

    def content(self, response):

        chrome_options = Options()

        prefs = {
            "profile.managed_default_content_settings.images": 2,
            "profile.content_settings.plugin_whitelist.adobe-flash-player": 2,
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 2,

        }
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_experimental_option('prefs', prefs)

        browser = webdriver.Chrome(chrome_options=chrome_options)
        browser.get(response.url)
        time.sleep(3)
        url = browser.find_element_by_class_name('mp-h5-player-layer-video').find_element_by_tag_name('video')\
            .get_attribute('src')
        item = MeipaiItem()

        # item['name'] = str(uuid.uuid1())

        item['url'] = url
        yield item












