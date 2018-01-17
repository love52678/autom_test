import re
from pprint import pprint
import requests
url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8955'
r = requests.get(url)
result = r.text
results = re.findall(r'([\u4e00-\u9fa5]+)\|([A-Z]+)', result)
results = dict(results)

print(results.keys())
print(results.values())
