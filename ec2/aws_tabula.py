#!/usr/bin/env python3

from tabulate import tabulate
from prettytable import PrettyTable

class CreateTable:

    def list_table(self,table_list :list):
        t = PrettyTable(['Instance ID','Name','Private IP','Public IP','Status'])
        tlist = []
        for i in table_list:
            tlist.append(i['Instance-Id'])
            tlist.append(i['Tag'])
            tlist.append(i['Private-IP'])
            tlist.append(i['Public-IP'])
            tlist.append(i['Status'])
            t.add_row(tlist)
            tlist = []
        print(t)