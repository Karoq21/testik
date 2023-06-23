from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
# автотест Блокировка карты на сайте idemo.bspb.ru по причине "Украдена"
s=Service('D:/CrDrv/chromedriver.exe')
driver = webdriver.Chrome(service = s)
driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
#time.sleep(5)
driver.set_window_size(1366, 768)
#Вход на сайт
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.ID, "login-otp-button").click()
time.sleep(2)
#Переходим на страницу Карты
driver.find_element(By.ID, "cards-overview-index").click()
time.sleep(2)
#Нажимаем кнопку блокировать
driver.find_element(By.XPATH, '//*[@id="card-details-ownbank-10068"]/div[2]/div[2]/div/div/div[2]/a/span').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="block-card-reasons"]/label[3]/input').click()
time.sleep(2)
driver.find_element(By.ID, "block-card").click()