# _*_ coding:utf-8 _*_
import os
common_path = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.dirname(common_path)
#获取log路径
log_path = os.path.join(project_path,'log')
report_path = os.path.join(project_path,'reports')
print(report_path)