# -*- coding: utf-8 -*-

# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import os
from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline
from scrapy.utils.project import get_project_settings


class MeipaiPipeline(FilesPipeline):
    FILES_STORE = get_project_settings().get("FILES_STORE")

    def get_media_requests(self, item, info):
        video_url = item['url']
        yield scrapy.Request(video_url)

    def item_completed(self, results, item, info):
        file_paths = [x["path"] for ok, x in results if ok]

        # if not file_paths:
        #     raise DropItem("Item contains no videos")
        # os.rename(self.FILES_STORE + "/" + file_paths[0], self.FILES_STORE + "/" + item["name"] + ".mp4")
        item['name'] = file_paths[0]
        return item

    def file_path(self, request, response=None, info=None):
        file_name = str(request.url).split('=')[-1]
        kind_name = '.mp4'
        return '%s%s' % (file_name, kind_name)
        # path = urlparse(request.url).pat
