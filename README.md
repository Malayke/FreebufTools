# FreebufTools
一个爬取Freebuf上发布的所有工具的爬虫

## 使用方法

首先得安装Python的Scrapy框架，[戳我](http://doc.scrapy.org/en/latest/intro/install.html)查看安装方法

然后


下载源码
```shell
git clone https://github.com/Malayke/FreebufTools.git
```

进入爬虫目录

```shell
cd freebuf_tools
```

开始爬取

> 爬取之前需要手动算出一共有几页工具
比如，打开这个url: http://www.freebuf.com/tools/page/68 
page后面的68就是工具页面的数量，可以通过二分法分析出一共存在几页
然后在运行时加上参数｀total_page｀
eq:
如果算出有61页，则 total_page参数赋值为61
```
scrapy crawl fbtools -a total_page=61
```

等它爬取结束，在当前目录下会生成叫 **fbtools_utf8.json**的文件，

里面是爬取的所有数据的json格式，方便日后使用！
