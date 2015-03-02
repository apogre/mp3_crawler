# -*- coding: utf-8 -*-

# Scrapy settings for mp3 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mp3'

SPIDER_MODULES = ['mp3.spiders']
NEWSPIDER_MODULE = 'mp3.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mp3 (+http://www.yourdomain.com)'
# ITEM_PIPELINES = {'mp3.pipelines.MySQLStorePipeline':300}
