from playwright.sync_api import sync_playwright
import time

#Launch Playwright
playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
page = browser.new_page()
page.goto("https://quotes.toscrape.com/js/")
page.wait_for_selector("div.container")
time.sleep(3)

#Save HTML
data_html = []
for x in range(1, 4):
    time.sleep(4)
    items = page.content()
    with open(f'data_html_{x}.html', "w+", encoding="utf-8") as f:
        f.write(items)
    page.locator('div > nav > ul > li.next > a').click()

browser.close()
playwright.stop()



