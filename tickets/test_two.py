import requests
import re
# date = '2018-01-09'
# fromstation = 'SHH'
# tostation = 'VUQ'
#
# url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date,fromstation,tostation)
# r = requests.get(url)
# print(url)
# print(r.json())


# coding: utf-8
# import re
# import requests
from pprint import pprint
#
url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955'
r = requests.get(url)
# print(r.text)
result = r.text
results = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', result)
# print(results)
dic = dict(results)
# print(dic)
pprint(dic,indent=4)#indent=4,缩进4个空格

# dics = []
# for t in results:
#     dress = {}
#     dress[t[0]] = t[1]
#     dics.append(dress)
# print(dics)

# stations = re.findall(r'([A-Z]+)\|([a-z]+)', text)
# stations = dict(stations)
# stations = dict(zip(stations.values(), stations.keys()))
# pprint(stations, indent=4)


# import re
#
# stations = "@bjb|北京北|VAP|beijingbei|bjb|0@bjd|北京东|BOP|beijingdong|bjd|1@bji|北京|BJP|beijing|bj|"
# results = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', stations)
# print(results)
#
# print(dict(results))

#
# id = [1,2,3,4]
# username = ['Jack','John','Michel','Lisa']
# users = []
# for i in range(len(id)):
#     user = {}
#     user['id'] = id[i]
#     user['name'] = username[i]
#     users.append(user)
# print(users)