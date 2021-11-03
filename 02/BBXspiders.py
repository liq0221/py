import time

import requests
import json
def geturl():

    urlCompany = 'https://api.baoxianxia.com.cn/api/common/icCompany'
    urlDetail = 'https://api.baoxianxia.com.cn/api/common/icfind'

    dataCom = {
        'version': '1.6.9',
        'platCode': 'H5',
        'body': '{}'
    }

    rCompany = requests.post(url=urlCompany, data=dataCom).text
    compNameList = []
    for i in range(ord('A'), ord('Z') + 1):
        compName = json.loads(rCompany)['result'][chr(i)]
        if compName != []:
            for name in compName:
                compNameList.append(name['name'])
    fp = open('D:\\mr_xiaohei\\BXX\\BXX.TXT', '+a', encoding='utf-8')
    for name in compNameList:
        dataDet = {
            'version': '1.6.9',
            'platCode': 'H5',
            'body': '{"type":"0","company":"%s","keyword":""}' % name
        }
        rDetail = requests.post(url=urlDetail, data=dataDet).text
        pdf_links = [i['pdfUrl'] for i in json.loads(rDetail)['result']]
        productName = [i['product'] for i in json.loads(rDetail)['result']]
        for l in range(len(pdf_links)):
            fp.write(name + '\t' + productName[l] + '\t' + pdf_links[l] + '\n')
            print("companyName:{}\tproductName:{}\tpdfLinke:{}存储完毕".format(name, productName[l], pdf_links[l]))
    fp.close()
t1 = time.time()
date_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
hour_time = time.strftime("%H:%M:%S", time.localtime(time.time()))
print('开始时间：{}'.format(date_time + hour_time))
geturl()
date_time1 = time.strftime("%Y-%m-%d", time.localtime(time.time()))
hour_time1 = time.strftime("%H:%M:%S", time.localtime(time.time()))
print('结束时间：{}'.format(date_time1 + hour_time1))
print('总用时：',int(time.time()-t1)/60)
