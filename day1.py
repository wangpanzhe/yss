
import datetime
import time 
st = '17:47:55'
st = datetime.datetime.strptime(st, "%H:%M:%S")
et="23:06:23"
et = datetime.datetime.strptime(et, "%H:%M:%S")

# 相减得到秒数
seconds = (et- st).seconds

print(seconds/60/60)
hours=(et- st)
print(hours)
# day=(et- st).min