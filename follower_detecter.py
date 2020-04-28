from selenium import webdriver
import os
import time 
from selenium.webdriver.common.keys import Keys

container = []
driver = webdriver.Firefox()

driver.get("https://www.instagram.com/")

time.sleep(5)

username = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
password = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")

username.send_keys(os.environ.get('DB_USER_BROWSER'))
password.send_keys(os.environ.get('DB_INSTA_PASS'))
time.sleep(2)
login = driver.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[1]/div/form/div[4]/button").click()
time.sleep(5)
try:
	dodge = driver.find_element_by_class_name("aOOlW").click()
	time.sleep(1)
except:
	pass
profile = driver.find_element_by_xpath("//*[@id='react-root']/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a").click()
time.sleep(3)
followers = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
followers.click()

time.sleep(5)

jscommand = """
followers = document.querySelector(".isgrP")
followers.scrollTo(0, followers.scrollHeight);
var lenofPage=followers.scrollHeight;
return lenofPage;
"""

#<a class="FPmhX notranslate  _0imsa " title="horizont1905" href="/horizont1905/">horizont1905</a>
# <button class="aOOlW   HoLwm " tabindex="0">Şimdi Değil</button>
#/html/body/div[4]/div/div/div[3]/button[2]

lenofpage = driver.execute_script(jscommand)
match = False

while (match==False):
	lastCount = lenofpage
	time.sleep(1)
	lenofpage = driver.execute_script(jscommand)
	if lastCount == lenofpage:
		match=True


rl_followers = driver.find_elements_by_class_name("FPmhX")
for follower in rl_followers:
	container.append(follower.text)

sayaç = 0
for i in container:
	sayaç += 1



jscommand1 = """
exit_button = document.querySelector(".pbNvD")
"""
close_follower = driver.execute_script(jscommand1)
close_follower = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button").click()
time.sleep(3)


following = driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a")
following.click()
time.sleep(3)


jscommand3 = """
following = document.querySelector(".isgrP")
following.scrollTo(0, following.scrollHeight);
var lenofPage=following.scrollHeight;
return lenofPage;
"""

lenofpage = driver.execute_script(jscommand3)
match = False
while (match==False):
	lastCount = lenofpage
	time.sleep(1)
	lenofpage = driver.execute_script(jscommand3)
	if lastCount == lenofpage:
		match=True

container1 = []
rl_following = driver.find_elements_by_class_name("FPmhX")
for follower in rl_following:
	container1.append(follower.text)

sayaç1 = 0
for i in container1:
	sayaç1 += 1

time.sleep(3)

with open("takipci.txt", "w+", encoding="UTF-8") as f:
	for context in container:
		f.write(context+",")

with open("takip.txt", "w+", encoding="UTF-8") as f:
	for context in container1:
		f.write(context+",")


for i in container1:
	if i in container:
		pass
	else:
		print(i)




driver.close()