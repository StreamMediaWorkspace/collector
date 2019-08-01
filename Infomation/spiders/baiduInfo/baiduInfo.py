import scrapy
from urllib.parse import urlencode
from Infomation.items import InfomationItem
from scrapy.utils.project import get_project_settings
import sys
sys.path.append(""../)
import ScapyBase

class BaiduInfo(ScrapyBase):
    def __init__(self, keys):
        parseListRegularExpressions = ParseListRegularExpressions()
        parseListRegularExpressions.list = '//div[@id="content_left"]//div[@class="result"]'
        parseListRegularExpressions.link = './h3[@class="c-title"]/a/@href'
        ScrapyBase.__init__(self, keys, parseListRegularExpressions)

