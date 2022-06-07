import requests
from lxml import etree
import json
from openpyxl import Workbook

url="https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}
response=requests.get(url,headers=headers)
html=etree.HTML(response.text)
result=html.xpath('//*[@id="captain-config"]/text()')
result=json.loads(result[0])
result_out=result["component"][0]
result_in=result["component"][0]["caseList"]

wb=Workbook()
ws=wb.active
ws.title="国内疫情"
ws.append(['省份','新增确诊','现有确诊','累计确诊','治愈','死亡'])
for each in result_in:
    temp_list=[each['area'],each['nativeRelative'],each['confirmedRelative'],each['confirmed'],each['crued'],each['died']]
    ws.append(temp_list)
wb.save("data.csv")