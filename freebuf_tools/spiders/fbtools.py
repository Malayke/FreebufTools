import scrapy
from freebuf_tools.items import FreebufToolsItem


class Fbtools(scrapy.Spider):
  name = 'fbtools'
  allowed_domains = ["freebuf.com"]
  start_urls = [
    "http://www.freebuf.com/tools"
  ]
  
  def parse(self, response):
    # unicode(response.body.decode(response.encoding)).encode('utf-8')
    fb = FreebufToolsItem()
    tool_sum_peer_page = len(response.xpath('//*[@id="timeline"]/div'))
    for tool_id in range(1,tool_sum_peer_page + 1):
      fb['tool_desc'] = response.xpath('//*[@id="timeline"]/div['+str(tool_id)+']/div[2]/dl/dt/a/text()').extract()
      fb['tool_release_date'] =  response.xpath('//*[@id="timeline"]/div['+str(tool_id)+']/div[2]/dl/dd[1]/span[3]/text()').extract()
      fb['tool_url'] = response.xpath('//*[@id="timeline"]/div['+str(tool_id)+']/div[2]/dl/dt/a/@href').extract()
      print "%s" % (fb['tool_release_date'])
      print u''.join(fb['tool_desc']),
      print fb['tool_url']
      yield fb

    for tools_page in range(2,48):
      yield scrapy.Request('http://www.freebuf.com/tools/page/'+str(tools_page), callback=self.parse)
