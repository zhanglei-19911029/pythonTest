import time
from selenium import webdriver

# 1、创建Chrome实例 。
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
# 2、driver.get方法将定位在给定的URL的网页 。
driver.get("http://liferestart.syaro.io/view/")  # get接受url可以是如何网址，此处以百度为例


def main():
    input("导入文件。。。。")
    # 3、定位元素 。
    # 3.2、用id定位点击对象，用click()触发点击事件
    while True:
        print("立即重开")
        driver.find_element_by_id('restart').click()
        #time.sleep(0.2)  # 延迟3秒
        print("10连抽")
        driver.find_element_by_id('random').click()
        #time.sleep(0.2)  # 延迟3秒
        print("天赋抽卡")
        text = driver.find_element_by_id("talents").text
        print(text)
        if "小盒子" in text:
            return
        driver.find_elements_by_class_name("grade0b")[0].click()
        driver.find_elements_by_class_name("grade0b")[1].click()
        driver.find_elements_by_class_name("grade0b")[2].click()
        #time.sleep(0.2)
        print("开始新人生")
        driver.find_element_by_id('next').click()
        #time.sleep(0.2)  # 延迟3秒
        print("随机分配")
        driver.find_element_by_id('random').click()
        #time.sleep(0.2)  # 延迟3秒
        print("开始新人生")
        driver.find_element_by_id('start').click()
        #time.sleep(0.2)  # 延迟3秒
        print("等待死亡，人生总结")
        try:
            driver.find_element_by_id('auto2x').click()  # 人生总结
        except:
            pass
        while True:
            try:
                driver.find_element_by_id('summary').click()  # 人生总结
                time.sleep(0.2)  # 延迟3秒
                break
            except:
                pass

        print("再次重开")
        driver.find_element_by_id('again').click()  # 人生总结
    # 4、退出访问的实例网站。
    # driver.quit()


main()
