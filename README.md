# Scrapy-Project

### 1. MySpider

1. 网址：http://cn.match.com
2. 由于该网站一次最多只能加载2000个用户，所以要分别爬取各个国家城市的用户信息。
3. 网站上的国家对应的编号CountryCode是js动态加载的。
    - 返回的json中有个'HasStates'字段,判断是否为True，生成不同的city_url。
        ```
        if country['HasStates']:
                curl = 'http://cn.match.com/MainService//GetStatesByCountryCode?countryCode='+str(country['Code'])
            else:
                curl = 'http://cn.match.com/MainService//GetCitiesByCountryCode?countryCode='+str(country['Code'])
        ```
    - 最后得到所有城市的搜索url，保存到本地，供读取使用。
4. 重写start_requests()方法，读取所有城市的url，发送请求。
5. 返回json数据，使用parse()解析，
    - 首先获取当前页，用来翻页爬取。
    - 请求每个用户页面。
6. parse_item()解析用户页面，获取用户所有图像url，返回item。
7. 在pipelines中自定义MyspiderPipeline类，继承ImagesPipeline，下个每个图像保存格式为 项目名/user_id/图像名

### 2. 小红书

1. 网址：https://www.xiaohongshu.com
2. 首先爬取所有的帖子，把用户id和帖子id存储到mongodb中。
3. 读取所有用户/帖子id，构造含有用户id的request headers，发送到
    ```
    url = 'https://www.xiaohongshu.com/web_api/sns/v1/note/{}/image_stickers'.format(item['t_id'])
    ```
4. 解析json数据，返回item。

### 3. 中国红娘网

1. 网址：http://www.hongniang.com
2. 从搜索的第一页开始爬取，在parse()中使用xpath解析页面，获取user_id，使用正则匹配用户age，循环发送用户页面请求，然后翻页。
3. parse_item()使用xpath解析页面，获取用户图像url，返回item

### 4. 马蜂窝

1. 网址：http://www.mafengwo.cn
2. 首先在网站中获取所有城市的编号，生成游记url，发送请求。
3. 在游记页面中获取用户个人url，进入后获取用户每个游记信息。
4. 进入每个游记，获取图像url，返回item。
5. 由于数据较多，在settings增加REDIS_HOST='10.8.3.6'，REDIS_PORT = 6379，更改为分布式，部署到服务器。

### 5. 我在找你

1. 网址：http://www.95195.com
2. 该网站有三个搜索用户接口，并且男女url不同，所以直接生成start_urls。
3. 在parse()中使用xpath匹配用户url，发送请求。
4. 在parse_item()使用xpath解析页面，获取用户图像url，返回item