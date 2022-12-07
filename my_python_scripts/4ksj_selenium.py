import os
from datetime import datetime
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


def screenshot(driver):
    path = 'downloads'
    if not os.path.exists(path):
        os.makedirs(path)
    driver.save_screenshot(f'{path}/{datetime.now()}.png')

def run():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('-incognito')
    options.add_argument('--remote-debugging-address=0.0.0.0')
    options.add_argument('--remote-debugging-port=5333')
    # options.add_argument("window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.4ksj.com/member.php?mod=logging&action=login")

    # try:
    #   title = WebDriverWait(driver, 10).until(
    #       lambda d: d.find_element(By.CSS_SELECTOR, "input[name=username]")
    #   )
    #   print(title.text)
    # except:
    #   driver.save_screenshot('snapshot.png')
    #   driver.quit()

    username_box = driver.find_element(by=By.CSS_SELECTOR, value="input[name=username]")
    password_box = driver.find_element(by=By.CSS_SELECTOR, value="input[name=password]")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button[name=loginsubmit]")

    username_box.send_keys("272077995@qq.com")
    password_box.send_keys("kaixin1234")
    # sleep(1)
    # print(submit_button.text)
    submit_button.click()
    # submit_button.send_keys(Keys.ENTER)
    # driver.execute_script('arguments[0].click();', submit_button)
    # ActionChains(driver).send_keys(Keys.ENTER).perform()

    try:
      title = WebDriverWait(driver, 5).until(
          lambda d: d.find_element(By.CSS_SELECTOR, "#mumucms_username")
      )
      print(title.text)
    except:
      print('error!')
    finally:
      screenshot(driver)
      driver.quit()
    # input('type to exit')
    # driver.quit()


if __name__ == '__main__':
    run()