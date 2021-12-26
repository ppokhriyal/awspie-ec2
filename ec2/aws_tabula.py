#!/usr/bin/env python3

import collections
from prettytable import PrettyTable
import pandas as pd

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

class GenerateReport:
    def genreport(self,table_list :list,reportname :str):
    
       df = pd.DataFrame(data=table_list,columns=['Instance-Id','Tag','Private-IP','Public-IP','Status'])
       df.to_excel(reportname+'.xlsx')
       
