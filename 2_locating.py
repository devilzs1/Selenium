from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://github.com/devilzs1"

driver.get(url)

driver.maximize_window()

title = driver.title
print(title)

assert "Mohammad Adil" in title


#Locating elements using CLASS_NAME
name = driver.find_element(By.CLASS_NAME, "vcard-fullname")
username = driver.find_element(By.CLASS_NAME, "vcard-username")

print("Name: " , name.text)
print("username: " , username.text)


#Locating elements using LINK_TEXT
achievements = driver.find_element(By.LINK_TEXT, "Achievements")
achievements_url = achievements.get_attribute("href")
print("Achievements " , f"{achievements_url}")


#Locating elements using PARTIAL_LINK_TEXT
followers = driver.find_element(By.PARTIAL_LINK_TEXT, "followers");
following = driver.find_element(By.PARTIAL_LINK_TEXT, "following");

print("Followers: ", followers.text)
print("Following: " , following.text)



#Locating elements using ID
# pinned_repo = driver.find_element(By.ID, "user-97207850-pinned-items-reorder-form")
# print("Pinned repositories: ", pinned_repo)

#Locating elements using NAME
#Locating elements using TAG_NAME
#Locating elements using CSS_SELECTOR
#Locating elements using XPATH

driver.quit()
