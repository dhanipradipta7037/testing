from playwright.sync_api import sync_playwright
import time

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://quotes.toscrape.com/js/")
page.wait_for_selector("div.container")
time.sleep(4)

data = []
for i in range(5):
    items = page.locator('div.quote').all()
    for item in items:
        text = item.locator('span.text').inner_text()
        list_text = {'Text':text}
        data.append(list_text)
    page.locator('div > nav > ul > li.next > a').click()
    time.sleep(4)

for x in data:
    print(x)

browser.close()
playwright.stop()