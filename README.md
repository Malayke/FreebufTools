# FreebufTools
一个爬取Freebuf上发布的所有工具的爬虫

## 使用方法

首先得安装Python的Scrapy框架，[戳我](https://scrapy-chs.readthedocs.org/zh_CN/0.24/intro/install.html)查看中文安装方法

然后

```
下载源码
git clone https://github.com/Malayke/FreebufTools.git

进入爬虫目录
cd freebuf_tools

开始爬取
scrapy crawl fbtools
```

等他爬取结束，在当前目录下会生成叫 **fbtools_utf8.json**的文件，

里面是爬取的所有数据的json格式，方便日后使用！
