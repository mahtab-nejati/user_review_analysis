from selenium import webdriver
import time

link = "https://play.google.com/store/apps/details?id=air.com.rosettastone.mobile.CoursePlayer&hl=en&showAllReviews=true"
driver = webdriver.Chrome("./chromedriver")
driver.get(link)
# element = driver.find_element_by_xpath(
#     "//div[span/text()='Most relevant']").click()
# time.sleep(1)
# element = driver.find_element_by_xpath("//div[span/text()='Newest']").click()
# time.sleep(3)

flag = 0
while 1:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    reviews = driver.find_elements_by_xpath(
        "//*[@jsname='fk8dgd']//div[@class='d15Mdf bAhLNe']")
    l = len(reviews)
    if l % 100 == 0:
        print("Reviews gathered so far: " + str(l))
    if l >= 5000:
        break
    try:
        loadMore = driver.find_element_by_xpath(
            "//*[contains(@class,'U26fgb O0WRkf oG5Srb C0oVfc n9lfJ')]").click()
    except:
        time.sleep(1)
        flag = flag+1
        if flag >= 10:
            break
    else:
        flag = 0

reviews = driver.find_elements_by_xpath(
    "//*[@jsname='fk8dgd']//div[@class='d15Mdf bAhLNe']")
print('GATHERED A TOTAL OF '+str(len(reviews))+' REVIEWS!!!')
with open("./dataset/source_rosettastone.html", "w+") as f:
    f.write(driver.page_source)
