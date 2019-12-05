import csv
import codecs
import json

import requests
from lxml import etree


# 访问网页，获取页面
def my_requests(context, page_start):
    url = f"https://www.amazon.cn/s?k={context}&page={page_start}&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&qid=1575340392&ref=sr_pg_2"

    headers = {
        'Host': 'www.amazon.cn',
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36",
        "Cookie": "x-wl-uid=1Je8WIvdDocW09uTylYcFy7io4fWWv3cAkmAZAIOSGLIR5DJSaZGFK++m6aG3QaiI6h28fVLbxNo=; session-id=460-7865641-7907136; ubid-acbcn=462-7676516-8549529; lc-acbcn=zh_CN; i18n-prefs=CNY; session-token=hUAKMb3vAeH95IddB0BLm8w1AMvDWi/DS2l1OdGYLmDyYUM8imFKbr4AXetzl00Pisq1M26qrJgTKQR+yjIPoBY1drxSOwprK+U8i//Eyrumc8gAThm3wcZaSe+bXb3DoWrNgieu6O3R5uz1Z+F2/i1tYtAt72Ge1h6pWZkGtQCU3eL849LYZ0D3Sl2Pf/HZ; session-id-time=2082729601l; csm-hit=tb:EFCJTXZG4KHYTWN67DG4+s-5ZCNYJXXMTXZCFRE4TCE|1575341483647&t:1575341483647&adb:adblk_no"
    }

    response = requests.get(url, headers=headers)
    html = response.text
    return html


def get_max_page(html):
    xpath_html = etree.HTML(html)
    try:
        max_page = xpath_html.xpath(
            '//div[@class="sg-row"]/div[last()]/div/span[last()-3]//div[@class="a-text-center"]//li[last()-1]/text()')
        return int(max_page[0])
    except IndexError:  # 当抛出异常时， 即没有找到该商品
        return None



# 解析页面， 提取数据
def my_spider(html,filepath, **print_format):
    xpath_html = etree.HTML(html)
    ware_list = xpath_html.xpath(
        '//div/div[@class="sg-col-inner"]/span[@cel_widget_id="SEARCH_RESULTS-SEARCH_RESULTS"]/div/div/div[@class="sg-row"][2]')
    for i in range(len(ware_list)):
        ware_dict = {}
        pformat = list(print_format.values())
        link = ware_list[i].xpath('string(./div[3]/div/div/h2/a/@href)')  # 获取详情链接
        ware_dict["商品连接"] = "https://www.amazon.cn" + link
        if pformat[0] == 1:
            ware_name = ware_list[i].xpath('string(./div[3]/div/div/h2/a/span)')  # 获取商品信息
            ware_dict["商品标题"] = ware_name
        if pformat[1] == 1:
            try:
                preic = ware_list[i].xpath('./div[4]/div/div[1]/div/div/a/span/span[1]/text()')[0].strip()  # 商品价格
            except IndexError as e:
                preic = ware_list[i].xpath('./div[4]/div/div/div[1]/span/span/text()')
            ware_dict["价格"] = preic
        if pformat[2] == 1:
            commect = ware_list[i].xpath('string(./div[3]/div/div[2]/div/span[last()])').strip()  # 评论数
            if commect == "":
                commect = "暂无评论"
            ware_dict["评论数"] = commect
        betrieb(filepath, ware_dict)


# 数据保存
def betrieb(fliepath, ware_dict):
    if fliepath[-4:] == ".csv":
        with open(fliepath, "a+", encoding="utf-8", newline='') as f:
            csv_writer = csv.writer(f)
            with open(fliepath, "r", encoding="utf-8", newline='') as f2:
                reader = csv.reader(f2)
                if not [row for row in reader]:
                    csv_writer.writerow(list(ware_dict.keys()))
                    csv_writer.writerow(list(ware_dict.values()))
                else:
                    csv_writer.writerow(list(ware_dict.values()))
    else:
        with open(fliepath, "a",  encoding="utf-8") as f:
            f.write(json.dumps(ware_dict, ensure_ascii=False) + "\n")



# if __name__ == '__main__':
#     html = my_requests("游戏王", 1)
#     max_page = get_max_page(html)
#     print(max_page)
#     my_spider(html, './1.csv', **{'title': 1, 'price': 1, 'comment': 1, 'comdetail': 0})