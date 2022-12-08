import json
import os

from dotenv import load_dotenv
from loguru import logger


def run():
    load_dotenv()
    logger.info("Hello World!")
    print(os.getenv("USERNAME1"))
    accounts = os.getenv("4K_ACCOUNTS")
    if accounts:
        print(json.loads(accounts)[0]["u"])


if __name__ == "__main__":
    run()
