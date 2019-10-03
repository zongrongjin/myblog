from config import article_list
import requests, re

def get_useful():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

    for i in article_list:
        url = i['url']
        res = requests.get(url, headers=headers).text
        i['useful'] = re.findall(r'赞同 (.*?)"', res)[0]

    return article_list