﻿"""Train tickets query via command-line.

Usage:
   tickets [-gdtkz] <from> <to> <date>

Options:
   -h,--help   显示帮助菜单
   -g          高铁
   -d          动车
   -t           特快
   -k          快速
   -z          直达

Example:
   tickets 上海 北京 2017-12-05
"""
from docopt import docopt
from stations import stations
import requests

def cli():
   """command-line interface"""
   arguments = docopt(__doc__)
   print(arguments['<date>'],arguments['<from>'],arguments['<to>'])
   date = arguments['<date>']
   fromstation = stations.get(arguments['<from>'])
   tostation = stations.get(arguments['<to>'])
   url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(date,fromstation,tostation)
   r = requests.get(url)
   print(url)
   print(r.json())

if __name__ == '__main__':
   cli()