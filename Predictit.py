from bs4 import BeautifulSoup
import bs4 as bs
import urllib.request
import requests
import json
import schedule
import time
from twilio.rest import Client
from selenium import webdriver
from selenium_stealth import stealth
from selenium.webdriver.common.keys import Keys

account_sid = #account_sid
auth_token = #auth_toekn

myPhone = #myPhone
TwilioNumber = #TwiloNumber

def predictRisk():
    url2 = "https://www.predictit.org/api/marketdata/all/"
    r = requests.get(url2)

    x = r.json()
    y = json.dumps(x)
    z = json.loads(y)
    i = 0
    x = 0
    w = -1
    u = 0
    total = 0.0
    howManyNoShares = 0
    t = 0
        #print(z)

        #print(z['markets'][0])


    for dictionary in z['markets']:
        i = i + 1
    print(i)

    while x < i:

        for dictionary in z['markets'][x]['contracts']:
            w = w+1
        while u <= w:
            noCost = (z['markets'][x]['contracts'][u]['bestBuyNoCost'])
            #print(noCost)
            if noCost is not None:
                total += 1.0 - noCost
                howManyNoShares = howManyNoShares+1
            u = u+1

        if(total >= 1.04):
            url = z['markets'][x]['url']
            Path = '/Users/andrestrujillo/PycharmProjects/Predictit/chromedriver 6'
            driver = webdriver.chrome(Path)

            #open url
            driver.get(url)
            #driver.maximize_window()
            time.sleep(2)

            #login to my acount
            login = driver.find_element_by_xpath('//*[@id="login"]').click()
            username = driver.find_element_by_xpath('//*[@id="username"]').send_keys()#username
            password = driver.find_element_by_xpath('//*[@id="password"]').send_keys()#password
            submit = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div/div/div[2]/div/form/div/div[6]/button').click()
            time.sleep(10)
            #see if there are more contracts not shown
            if(len(driver.find_elements_by_css_selector("div#app div.market-detail div.market-detail__contracts div.market-detail__contracts-toggle-more")) > 0):
                morecontracts = driver.find_element_by_css_selector("div#app div.market-detail div.market-detail__contracts div.market-detail__contracts-toggle-more").click()

            #scroll to the top to not overlap elements
            driver.execute_script("window.scrollTo(0, 0)")


            list = driver.find_elements_by_class_name("market-contract-horizontal-v2__buttons--right")
            #buying contracts
            while t < len(list):
                time.sleep(2)
                if("N/A" not in driver.find_elements_by_class_name('market-contract-horizontal-v2__buttons--right')[t].text and 'Buy No' in driver.find_elements_by_class_name('market-contract-horizontal-v2__buttons--right')[t].text):
                    driver.find_elements_by_class_name("market-contract-horizontal-v2__buttons--right")[t].click()
                    time.sleep(5)
                    driver.find_elements_by_xpath('.button.button--primary.button--full-width.purchase-offer__footer-next-button').click()
                    driver.find_elements_by_css_selector('.button.button--primary.button--full-width.purchase-offer__footer-next-button').click
                    driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div/div/div[2]/div/div/div[6]/div[1]/div/button').click()
                    driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div/div/div[2]/div/div/div[4]/div[3]/div/button').click()


                if("N/A" not in driver.find_elements_by_class_name('market-contract-horizontal-v2__buttons--left')[t].text and 'Buy No' in driver.find_elements_by_class_name('market-contract-horizontal-v2__buttons--left')[t].text):
                    driver.find_elements_by_class_name("market-contract-horizontal-v2__buttons--left")[t].click()
                    time.sleep(5)
                    driver.find_elements_by_css_selector('.button.button--primary.button--full-width.purchase-offer__footer-next-button').click
                    driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div/div/div[2]/div/div/div[6]/div[1]/div/button').click()
                    driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div/div/div[2]/div/div/div[4]/div[3]/div/button').click()

                t = t+1

        else:
            print("no negative risk =(")

        u=0
        w = -1
        total = 0.0
        x = x+1
        howManyNoShares = 0
        t=0



schedule.every(25).seconds.do(predictRisk)

while True:
    schedule.run_pending()
    time.sleep(1)





