import os
from time import strftime


def screenshot(driver):
    path = "downloads"
    timeformat = "%Y_%m_%d-%I_%M_%S_%p"
    if not os.path.exists(path):
        os.makedirs(path)
    driver.save_screenshot(f"{path}/{strftime(timeformat)}.png")
