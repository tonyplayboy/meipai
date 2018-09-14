from scrapy import cmdline
name = 'meipai'
cmd = 'scrapy crawl {0}'.format(name)
cmdline.execute(cmd.split())
