#!/usr/bin/env python
# coding=utf-8
#detetime
import re
from datetime import datetime, timezone, timedelta
def to_timestamp(dt_str, tz_str):
    times = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
#    dt = datetime(times)
    time1 = re.match(r'^(\w{3})\+(\d{1})(\:+\d{2})$',tz_str).group(2)
    ds = 8 - int(time1)
    print(ds)
    timeover = times + timedelta(hours = ds)
    print(timeover.timestamp())

#    print(dt)

t1 = to_timestamp('2015-1-21 9:01:30', 'UTC+5:00')
