import requests
import json
# import chardet
# import re
# import codecs
# import gzip

'''
使用时候只要import这个文件然后在需要信息的地方使用fun.main()
就可以生成当前天气情况now.json 新闻信息news.json 未来三天天气forecast.json

文件读取后格式为：
now.json : {'results': [{'now': {'temperature': '15', 'code': '4', 'text': '多云'}, 'last_update': '2017-11-04T15:44:00+08:00', 'location': {'timezone_offset': '+08:00', 'timezone': 'Asia/Shanghai', 'path': '上海,上海,中国', 'id': 'WTW3SJ5ZBJUY', 'name': '上海', 'country': 'CN'}}]}

news.json : {['百度', '新闻1', '新闻2'], ['新浪', '新闻3', '新闻4'], ['腾讯', '新闻5', '新闻6']}
（一个列表中包含三个列表 每个列表第一个都是该网站的名字 从第二个开始是新闻标题）
forecast.json : {'results': [{'location': {'name': '上海', 'timezone': 'Asia/Shanghai', 'path': '上海,上海,中国', 'id': 'WTW3SJ5ZBJUY', 'timezone_offset': '+08:00', 'country': 'CN'}, 'daily': [{'text_day': '多云', 'wind_scale': '2', 'text_night': '多云', 'precip': '', 'wind_speed': '10', 'high': '16', 'code_night': '4', 'date': '2017-11-04', 'wind_direction': '东北', 'code_day': '4', 'low': '11', 'wind_direction_degree': '45'}, {'text_day': '多云', 'wind_scale': '2', 'text_night': '多云', 'precip': '', 'wind_speed': '10', 'high': '17', 'code_night': '4', 'date': '2017-11-05', 'wind_direction': '东', 'code_day': '4', 'low': '12', 'wind_direction_degree': '90'}, {'text_day': '多云', 'wind_scale': '2', 'text_night': '多云', 'precip': '', 'wind_speed': '10', 'high': '22', 'code_night': '4', 'date': '2017-11-06', 'wind_direction': '东南', 'code_day': '4', 'low': '16', 'wind_direction_degree': '135'}], 'last_update': '2017-11-04T11:00:00+08:00'}]}
'''
news = []

def main():
    url = ['http://news.baidu.com/', 'http://news.sina.com.cn/', 'https://news.qq.com']
    url_bd = ['guonei', 'guoji', 'society']
    url_xl = ['china', 'world', 'society']

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
    }
    params = {
        'key': 'KEY',
        'location': 'LOCATION',
        'language': 'LANGUAGE',
        'unit': 'UNIT'
    }
    s = requests.session()

    # '''
    # 百度
    news_bd = ['百度']
    for y in url_bd:
        response = s.get(url[0] + y, headers=headers)
        html = response.text
        start = html.find('即时新闻')
        # print(start)
        end = html.find('<li class="item report button-rotate" data-text="举报">')
        # print(end)
        while True:
            start = html.find('target="_blank"', start)
            start = html.find('>', start)
            tmp = html.find('<', start, end)
            if tmp == -1:
                break
            if tmp - start > 18 or tmp - start < 7:
                continue
            data = html[start+1:tmp]
            if data not in news_bd:
                news_bd.append(data)
                # print(data)
            start = tmp
        # with codecs.open('baidu' + y + '.html', 'w', encoding='utf-8') as f:
        #     f.write(html)
    news.append(news_bd)
    # '''

    # '''
    # 新浪
    news_xl = ['新浪']
    for y in url_xl:
        response = s.get(url[1] + y, headers=headers)
        content = response.content
        html = content.decode()
        start = html.find('<!-- seo内容输出 -->')
        end = html.find('<!-- seo内容输出 -->', start+10)
        while True:
            start = html.find('target="_blank"', start)
            start = html.find('>', start)
            tmp = html.find('</a></li>', start)
            if tmp == -1:
                break
            data = html[start+1:tmp]
            if data[:2] == '视频':
                start = tmp
                continue
            # print(data)
            news_xl.append(data)
            start = tmp
        # with open('sina' + y + '.html', 'w') as f:
        #     f.write(html)
    news.append(news_xl)
    # '''

    # '''
    # 腾讯
    news_tx = ['腾讯']
    response = s.get(url[2], headers=headers)
    content = response.content
    html = content.decode('gbk')
    start = html.find('热度排行')
    end = html.find('<!-- 排行end -->', start)
    while True:
        start = html.find('target="_blank">', start)
        tmp = html.find('</a></li>', start, end)
        if tmp == -1:
            break
        data = html[start+16:tmp]
        # print(data)
        news_tx.append(data)
        start = tmp
    news.append(news_tx)
    # '''
# '''
    def fetchWeather():
        response = requests.get('https://api.seniverse.com/v3/weather/now.json', params={
            'key': 'y2nmh7jzqjsq0y2w',
            'location': 'ip',
            'language': 'zh-Hans',
            'unit': 'c'
        }, timeout=1)
        content = json.loads(response.content.decode())
        with open('now.json', 'w') as f:
            json.dump(content, f)

        response = requests.get('https://api.seniverse.com/v3/weather/daily.json', params={
            'key': 'y2nmh7jzqjsq0y2w',
            'location': 'ip',
            'language': 'zh-Hans',
            'unit': 'c',
            'start': '0',
            'days': '3'
        }, timeout=1)
        content = json.loads(response.content.decode())
        with open('forecast.json', 'w') as f:
            json.dump(content, f)

    fetchWeather()
    # with open('news.json', 'w') as f:
    #     json.dump(news, f)
# '''
    return news

if __name__ == '__main__':
    a = main()
    print(a)
