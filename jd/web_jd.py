from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from lxml import etree
import time
import os
import xlwt


driver=webdriver.Chrome()
driver.maximize_window()
# os.path.join('/home/cy/PycharmProjects/爬虫实战/taobao','outdata')



info_list = []
def get_info(url):
    driver.get(url)
    driver.implicitly_wait(10)
    selector=etree.HTML(driver.page_source)
    infos=selector.xpath('//*[@id="J_goodsList"]/ul')
    for info in infos:
        name=info.xpath(ele1)
        price=info.xpath(ele2)
        quriment=info.xpath(ele3)
        comment=info.xpath(ele4)
        seller=info.xpath(ele5)
        info_list1=[name,price,quriment,comment,seller]
        info_list.append(info_list1)

        # jd={
        #     "name":name,
        #     "price":price,
        #     "quriment":quriment,
        #     "comment":comment,
        #     "seller":seller
        #
        # }
        # // *[ @ id = "J_goodsList"] / ul / li[91] / div / div[3] / a / em / text()[1]
    #
    # // *[ @ id = "J_goodsList"] / ul / li[1] / div / div[3] / a / em / text()[1]

    # // *[ @ id = "J_goodsList"] / ul / li[1] / div / div[2] / strong / i
    # info_list.append(jd)

    # // *[ @ id = "J_goodsList"] / ul / li[1] / div / div[3] / a / em / text()[1]

    # // *[ @ id = "J_goodsList"] / ul / li[1] / div / div[3] / a / em / text()[1]
    # // *[ @ id = "J_goodsList"] / ul / li[2] / div / div[3] / a / em / text()[1]
    #
    # // *[ @ id = "J_goodsList"] / ul / li[4] / div / div[3] / a / em / text()[1]
    # // *[ @ id = "J_goodsList"] / ul / li[60] / div / div[3] / a / em / text()[1]
    # print(driver.page_source)

    # // *[ @ id = "J_goodsList"] / ul / li[13] / div / div[3] / a / em / text()[2]


if __name__=="__main__":

    # url="http://www.taobao.com/"
    url = "https://www.jd.com/"

    driver.get(url)
    driver.implicitly_wait(10)

    # driver=driver.find_element_by_id('q').clear()
#     element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, 'q')))
#     element.send_keys('男士短袖')
#     driver.find_element_by_class_name("btn-search").click()
# #点击登录按钮
#     driver.find_element_by_xpath('//*[@id="J_QRCodeLogin"]/div[5]/a[1]').click()
#
#     element=driver.find_element_by_xpath('//*[@id="J_Form"]/div[2]/span').click()
#     element.send_keys('阳子小娅')
#     time.sleep(1)
#     element=driver.find_element_by_xpath('//*[@id="TPL_password_1"]').click()
#     element.send_keys('cy12061228')
#     time.sleep(1)
#     driver.find_element_by_xpath('//*[@id="J_SubmitStatic"]').click()

    element = WebDriverWait(driver, 5, 0.5).until(EC.presence_of_element_located((By.ID, 'key')))
    element.send_keys('笔记本')
    element.send_keys(Keys.ENTER)  #回车键点击登录
    time.sleep(1)

    eles1= ['li[{0}]/div/div[3]/a/em/text()[1]'.format(str(i)) for i in range(1, 31)]
    eles2= ['li[{0}]/div/div[2]/strong/i/text()'.format(str(i)) for i in range(1, 31)]
    eles3 = ['li[{0}]/div/div[3]/a/em/text()[2]'.format(str(i)) for i in range(1, 31)]
    eles4 = ['li[{0}]/div/div[4]/strong/a/text()'.format(str(i)) for i in range(1, 31)]
    eles5 = ['li[{0}]/div/div[5]/span/a/text()'.format(str(i)) for i in range(1, 31)]
    for ele1,ele2,ele3,ele4,ele5 in zip(eles1,eles2,eles3,eles4,eles5):

        get_info(driver.current_url)

    print(info_list)

    header=['name','price','peizhi','com_data','seller']
    book=xlwt.Workbook(encoding='utf-8')
    sheet=book.add_sheet('Sheet1')
    for h in range(len(header)):
        sheet.write(0,h,header[h])

    i=1
    for list in info_list:
        j=0
        for data in list:
            sheet.write(i,j,data)
            j+=1
        i+=1
    book.save('jd2_data.xls')
# //*[@id="J_goodsList"]/ul/li[1]/div/div[5]/span/a
# //*[@id="J_goodsList"]/ul/li[4]/div/div[5]/span/a
# //*[@id="J_goodsList"]/ul/li[60]/div/div[2]/strong/i