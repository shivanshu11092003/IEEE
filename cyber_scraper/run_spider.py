import os
import schedule
import time

def run_spider():
    os.system('scrapy crawl cyber_incident -o output.json')


run_spider()

schedule.every(12).hours.do(run_spider)

while True:
    schedule.run_pending()
    time.sleep(1)
