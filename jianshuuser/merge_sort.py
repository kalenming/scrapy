# import matplotlib.pyplot as plt
#
# import numpy as np
#
# labels='A','B','C','D','E','F'
#
# y = [5652,20561,12000,218268, 27500,778]
#
# plt.axes(aspect=1)  # 使x y轴比例相同
#
# explode = [0, 0.05, 0, 0, 0, 0]  # 突出某一部分区域
#
# plt.pie(x=y, labels=labels, autopct='%.0f%%', explode=explode)  # autopct显示百分比
#
# plt.show()
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
pf = pd.read_excel(r'C:\Users\Administrator\Desktop\week_report\data_3.xlsx')
data = pf[pf['资金方'] == "深圳鑫科国际商业保理有限公司"]
#print (type(data))
business_loan = data.groupby('电商')['下单金额'].count()
labels = list(business_loan.index)
print (labels)
y = list(business_loan.values)
print (y)
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.axes(aspect=1)  # 使x y轴比例相同
# explode = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05 ,0.05 ,0.05]  # 突出某一部分区域
#
# colors  = ["blue","red","coral","green","yellow","orange","yellow","white"]
# plt.pie(x=y, labels=labels, autopct='%.0f%%',colors = colors, explode=explode,pctdistance=0.8, shadow=True)  # autopct显示百分比
#
# plt.show()


plt.bar(labels, y, color='rgb') # or `color=['r', 'g', 'b']`
plt.show()