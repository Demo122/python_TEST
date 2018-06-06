#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@auther:danqing
@time:2018/6/6 23:25
"""
#将以数指定的年，月，日的日期打印出来

months = ['January','February','March','April','May','June','July','August','September','October','November','December']

#一个列表，其中包含数1-31对应的结尾
endings = ['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']

year  = input('Year: ')
month = input('Month(1-12): ')
day   = input('Day(1-31): ')

month_number = int(month)-1
day_number =int(day)-1

print("以数指定的年，月，日的日期为：",months[month_number] +' '+ day+endings[day_number] + ',' + year)
