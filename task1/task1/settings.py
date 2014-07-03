# -*- coding: utf-8 -*-

# Scrapy settings for task1 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'livingsocial'

SPIDER_MODULES = ['task1.spiders']
NEWSPIDER_MODULE = 'task1.spiders'

DATABASE = {'drivername': 'mysql+mysqlconnector',
            'host': 'localhost',
            'port': '3306',
            'username': 'root',
            'password': '123123',
            'database': 'scrapylivesocial'}

ITEM_PIPELINES = ['task1.pipelines.LivingSocialPipeline']

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'task1 (+http://www.yourdomain.com)'
