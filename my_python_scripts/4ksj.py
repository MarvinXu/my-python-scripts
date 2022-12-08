import os

import requests
from dotenv import load_dotenv

load_dotenv()
USERNAME = os.getenv("USERNAME1")
PASSWORD = os.getenv("PASSWORD1")

with requests.Session() as s:

    r0 = s.post(
        "https://www.4ksj.com/member.php?mod=logging&action=login&loginsubmit=yes&inajax=1",
        data={"username": USERNAME, "password": PASSWORD},
    )
    r = s.get("https://www.4ksj.com/home.php?mod=space&do=doing&view=me")
    print(r.text.split("\n")[:10])

    # 签到请求不生效
    # r = s.get('https://www.4ksj.com//qiandao/?mod=sign&operation=qiandao&formhash=22fab891&format=empty&inajax=1&ajaxtarget=')
    # print(r.text)
