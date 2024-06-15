from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://github.com/devilzs1")

driver.maximize_window()

title = driver.title
print(title)

assert "Mohammad Adil" in title

driver.quit()
