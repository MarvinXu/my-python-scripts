import json
import os
from time import sleep

from dotenv import load_dotenv
from loguru import logger
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

from .util import screenshot


def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("-incognito")
    options.add_argument("--remote-debugging-address=0.0.0.0")
    options.add_argument("--remote-debugging-port=5333")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    )
    options.add_argument("window-size=1280,720")

    driver = webdriver.Chrome(options=options)

    return driver


def run():
    load_dotenv()
    accounts = json.loads(os.getenv("4K_ACCOUNTS") or "[]")

    if not accounts:
        return logger.error("no accounts found, cancel task.")

    for account in accounts:
        task(account)


# Sign in with account
def task(account):
    driver = setup_driver()

    USERNAME = account["u"]
    PASSWORD = account["p"]

    # Login
    try:
        driver.get("https://www.4ksj.com/member.php?mod=logging&action=login")
        username_box = driver.find_element(
            by=By.CSS_SELECTOR, value="input[name=username]"
        )
        password_box = driver.find_element(
            by=By.CSS_SELECTOR, value="input[name=password]"
        )
        submit_button = driver.find_element(
            by=By.CSS_SELECTOR, value="button[name=loginsubmit]"
        )
        username_box.send_keys(USERNAME)
        password_box.send_keys(PASSWORD)
        submit_button.click()
        logger.debug("Start Login...")

        # wait for page redirect
        profile = WebDriverWait(driver, 10).until(
            visibility_of_element_located((By.CSS_SELECTOR, "#mumucms_username"))
        )
        logger.success(f"Login success: {profile.text}")
    except:
        screenshot(driver)
        logger.error("Login failed!")
        return driver.quit()

    # Sign in
    try:
        driver.get("https://www.4ksj.com/qiandao/")
        signbtn = WebDriverWait(driver, 5).until(
            visibility_of_element_located((By.CSS_SELECTOR, "#JD_sign"))
        )
        signbtn.click()
        sleep(2)
        logger.success("Sign-in succeed!")
    except:
        logger.error("Sign-in failed!")
        screenshot(driver)
        return driver.quit()

    # Get result
    try:
        driver.get("https://www.4ksj.com/home.php?mod=spacecp&ac=credit&op=base")
        result = WebDriverWait(driver, 5).until(
            visibility_of_element_located((By.CSS_SELECTOR, "table tr:nth-child(2)"))
        )
        logger.info(result.text)
    except:
        logger.error("Get result failed!")
        screenshot(driver)

    driver.quit()


if __name__ == "__main__":
    run()
