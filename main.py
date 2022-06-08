import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/agnie/Developer/chromedriver.exe"

facebook_login = "annaanna.poczta1@gmail.com"
facebook_password = os.getenv("SHEET_API_PASS")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
driver.get("https://tinder.com/")
# save main window path
main_window = driver.current_window_handle
driver.implicitly_wait(15)

# log into tinder
driver.find_element(By.XPATH, '//*[@id="s1746966696"]/div/div[2]/div/div/div[1]/div[2]/button/span').click()
driver.find_element(By.XPATH, '//*[@id="s1746966696"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]'
                              '/div[2]/a/span').click()

sleep(3)
driver.find_element(By.XPATH, '//*[@id="s18585620"]/div/div/div[1]/div/div/div[3]/span/div[2]/button').click()

new_window = None
while not new_window:
    for handle in driver.window_handles:
        if handle != main_window:
            new_window = handle
            break

driver.implicitly_wait(10)
driver.switch_to.window(new_window)
#  click cookie
driver.find_element(By.CSS_SELECTOR, "div[class='_9xo5'] button").click()

#  log into facebook
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(facebook_login)
driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys(facebook_password)
driver.find_element(By.NAME, "login").click()

#  go back to main window
driver.switch_to.window(main_window)

# approve localization
driver.find_element(By.XPATH, '//*[@id="s18585620"]/div/div/div/div/div[3]/button[1]').click()

# no approve for notifications
driver.find_element(By.XPATH,'//*[@id="s18585620"]/div/div/div/div/div[3]/button[2]').click()

# tinder rejections
counter = 0
on_game = True
while on_game:
    sleep(2)
    if counter <= 100:
        driver.find_element(By.CSS_SELECTOR,'body').send_keys(Keys.LEFT)
        counter += 1
        try:
            # checking for window with mini tinder installation
            driver.implicitly_wait(0)
            driver.find_element(By.XPATH,'//*[@id="s18585620"]/div/div/div[2]/button[2]').click()
        except:
            pass
        finally:
            driver.implicitly_wait(4)
    else:
        print("Your daily amount of choosing is out.")
        break
