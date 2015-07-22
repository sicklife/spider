#豆瓣书评爬虫

这个爬虫，是按照时间顺序爬取书评，每次爬取5篇

每次爬取5篇，通过`setting.py`中的`CLOSESPIDER_ITMECOUNT`设定

用`basicspider`来写。

##遇到的错误合集

1. 页面会request两遍。因为在`url`最后少加了一个`\`，导致会多一次跳转

2. 遇到404页面爬虫会终止。在`spider`中添加了`handle_httpstatus_list=[404]`

3. `Spider must return Request, BaseItem, dict or None`错误的使用`yeild`做最后的`itme`返回。

4. 