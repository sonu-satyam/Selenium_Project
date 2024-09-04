from selenium.webdriver.firefox.webdriver import WebDriver
from time import sleep

driver = WebDriver()
driver.get("https://www.youtube.com/")

driver.maximize_window()
url_title = driver.title
url = driver.current_url
print(url_title)
print(url)

driver.find_element("xpath", "//input[@id='search']").send_keys("bulaya aayi nahi stree")
sleep(5)
driver.find_element("xpath", "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button/yt-icon/span/div").click()
sleep(5)
driver.find_element("xpath", "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[2]/div[1]/div/div[1]/div/h3/a/yt-formatted-string").click()

