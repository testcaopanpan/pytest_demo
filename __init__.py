# _*_ coding:utf-8 _*_
from datetime import datetime
name = "case"+datetime.now().date().strftime('%Y%m%d')+".log"
print(name)