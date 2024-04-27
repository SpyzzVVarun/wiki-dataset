from constants import LIMIT, page_db_links
from driver import driver
from selenium.webdriver.common.by import By

titles = []
for link in page_db_links:
    driver.get(link)
    for i in range(1, LIMIT+1):
        try:
            titles.append(driver.find_element(By.XPATH,f"//*[@id='mw-whatlinkshere-list']/li[{i}]/a").get_attribute("href").split("/")[-1])
        except:
            pass
    
with open("titles.txt", "w") as f:
    for title in titles:
         f.write(title + "\n")
    f.close()