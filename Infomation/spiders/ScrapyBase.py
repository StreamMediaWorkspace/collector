class ParseListRegularExpressions:
    def __init__(self):
        this.list = ""
        this.body = ""
        this.time = ""
        this.link = ""
        this.title = ""
        this.nextpage = ""


class ScrapyBase():
    def __init__(self, keys, parseListRegularExpressions):
        this.keys = keys
        this.parseListRegularExpressions = parseListRegularExpressions

    def start(self, urlFormat):
        for key in self.key_result:
            key = urllib.parse.quote(key, safe='/', encoding=None, errors=None)
            media_url = urlFormat.format(key)
            print(media_url)
            yield scrapy.Request(url=media_url, callback=self.weibo_parse)

    def parseList(self, response):
        print(response)
        info_list = response.xpath(self.parseListRegularExpressions.list)
        for info in info_list:
            item = InfomationItem()
            item['link'] = info.xpath(self.parseListRegularExpressions.link).extract_first()
            item['title'] = info.xpath(self.parseListRegularExpressions.title).extract_first()
            yield scrapy.Request(url=item['link'], callback=self.parseDatail)

    def parseDatail(self, response):
        print(response)
