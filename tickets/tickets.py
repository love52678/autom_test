"""Train tickets query via command-line.

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
   tickets 上海 北京 2018-01-13
"""
import stations
import requests
from docopt import docopt
from prettytable import PrettyTable
class Tickets():
    def printTrainInfo(self):
        arguments = docopt(__doc__)
        print(arguments['<date>'],arguments['<from>'],arguments['<to>'])
        date = arguments['<date>']
        fromstation = stations.getCode(arguments['<from>'])
        tostation = stations.getCode(arguments['<to>'])

        url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
            date, fromstation, tostation)
        r = requests.get(url)
        print(url)
        print(r.json())
        allresult = r.json()
        allTickets = allresult['date']['result']
        rows = self.parse_train(allTickets)
        self.printtable(rows)

    def parse_train(self,allTickets):
        rows = []
        for ticket in allTickets:
            trainrow = []
            trainlist = ticket.spit('|')
           # trainrow.extend(trainlist[3:6])
            trainlist[4] = stations.getCityName(trainlist[4])
            trainlist[5] = stations.getCityName(trainlist[5])
            trainrow.append(trainlist[3])
            trainrow.append(trainlist[4])
            trainrow.append(trainlist[5])
            trainrow.extend(trainlist[8:11])
            trainrow.extend(trainlist[32:21:-1])
            row = []
            for x in trainrow:
                x = x or '--'
                row.append(x)
            rows.append(row)
        return rows


    def printtable(self,rows):
       # x = PrettyTable(info)
        info = '车次 出发站 到达站 出发时间 历时 商务座 特等座 一等座 二等座 高级 软卧 动卧 硬卧 软座 硬座 无座'
        info.split(' ')
        x = PrettyTable(info)
        for row in rows:
            x.add_row(row)
        print(x.get_string())

if __name__ == '__main__':
    Tickets().printTrainInfo()