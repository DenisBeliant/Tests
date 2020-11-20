from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Test title : get homepage

driver = webdriver.Opera()
driver.get("http://polr.floki.io")

try:
    assert "My Polr" in driver.title
    assert "http://polr.floki.io/login" == driver.current_url
except:
    print("Impossible d'obtenir la home page")
# Pass

# Test title : give a valid credentials :

login = driver.find_elements(By.NAME, "username")[1]

driver.implicitly_wait(1)

login.send_keys("admin")

pswd = driver.find_elements(By.NAME, "password")[1]
pswd.send_keys("campus")

pswd.send_keys(Keys.ENTER)

driver.implicitly_wait(1)

menu = driver.find_element_by_xpath("/html/body/div[1]/nav/ul[2]/div/li/a")

menu.click()

listMenu = driver.find_elements_by_xpath("/html/body/div[1]/nav/ul[2]/div/li/ul/li")

try:
    assert "http://polr.floki.io/" == driver.current_url
except:
    print("impossible d'obtenir la page de shorter")

try:
    assert listMenu[0].text == "DASHBOARD"
    assert listMenu[1].text == "SETTINGS"
    assert listMenu[2].text == "LOGOUT"
except:
    print("les items de menu ne sont pas valide")
# Pass

# Test title : Invalid credentials :
"""
login = driver.find_elements(By.NAME, "username")[1]

driver.implicitly_wait(1)

login.send_keys("admineeeee")

pswd = driver.find_elements(By.NAME, "password")[1]
pswd.send_keys("campus")

pswd.send_keys(Keys.ENTER)

try:
    assert "http://polr.floki.io/login" == driver.current_url
catch:
    print("Pas de retour à la page de login")
"""
# Pass

# Test title : Get shorter webpage (same as "valid creditials" page, pass)

# Test title : Short an big url :
"""
login = driver.find_elements(By.NAME, "username")[1]

driver.implicitly_wait(1)

login.send_keys("admin")

pswd = driver.find_elements(By.NAME, "password")[1]
pswd.send_keys("campus")
pswd.send_keys(Keys.ENTER)

driver.implicitly_wait(3)

url = driver.find_elements(By.NAME, "link-url")[0]
url.send_keys("https://www.google.com/search?client=opera&hs=FGD&biw=1496&bih=791&sxsrf=ALeKk02IvMBSxO-fGjyDSZVHOyM1Rer4hA%3A1604858788829&ei=pDOoX5KHMsb0aPSWoLgK&q=parrot+zik+1+android+app&oq=parrot+zik+android+&gs_lcp=CgZwc3ktYWIQAxgBMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgjEK4CECc6BAgjECc6AggAOgUIABDLAVCQ6tICWIGH0wJg25XTAmgAcAB4AYABkQKIAfYXkgEGNi4xNi4ymAEAoAEBqgEHZ3dzLXdpesABAQ&sclient=psy-ab")

url.send_keys(Keys.ENTER)

try:
    assert "http://polr.floki.io/" != driver.current_url
except:
    print("Page de shorter non récupérée")

# Not pass
#driver.close()

"""