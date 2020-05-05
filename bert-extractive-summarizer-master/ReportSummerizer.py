from summarizer import Summarizer
from tkinter import filedialog
from tqdm import tqdm
import os
import re
import csv

model = Summarizer()

# 输入police_report文件夹路径
input_dir = filedialog.askdirectory(title='Select the input directory')
# input_dir = '/Users/liziyang/Downloads/NJIT_Sandbox-selected/Example_10'

# 将yy返回YYYY年份
def conv(yy):
    if int(yy) < 20:
        return int('20' + yy)
    else:
        return int('19' + yy)

report_content = []    #报告内容
report_summarized = []   #报告总结
report_name = []   #报告名称
date_list = []  #报告日期


for text in tqdm(os.listdir(input_dir)):
    complete_path = os.path.join(input_dir,text)
    with open(complete_path,'r',encoding='utf-8') as f:
        reader = f.read()
    result = model(reader, min_length=20, max_length=50)   # bert based pre trained uncased model
    date = re.search(r'RMS\d{2}', text)
    date = re.search(r'\d{2}', date.group())
    full_date = conv(date.group())  # 从文件名中提取年份
    date_list.append(full_date)
    report_content.append(reader)
    report_summarized.append(result)
    report_name.append(str(text).replace('.txt', ''))

print(len(report_content))
print(len(report_summarized))
print(len(report_name))
print(len(date_list))

with open('ReportSummerizer.csv','w',encoding='utf-8') as f:
    writer = csv.writer(f)
    header = ['ReportName','Date','ReportContent','SummarizedContent']
    writer.writerow(header)
    for i in range(len(report_content)):
        writer.writerow([report_name[i],date_list[i],report_content[i],report_summarized[i]])