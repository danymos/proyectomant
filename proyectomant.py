#MANTENIMIENTO
#CHANTAL DE GRACIA 8-971-1853    
# DANIELA MOSCOSO 8-977-974
#FECHA: NOV 11 

import pdb
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support.ui import Select

# waiting time between actions
WAIT_TIME = .5

# abrir chrome y amazon.com

driver = webdriver.Chrome('C:/selenium/chromedriver.exe')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")


# look up the text box
textbox = driver.find_element(By.ID, "twotabsearchtextbox")
sleep(WAIT_TIME)
# write HP Pavilion azul
textbox.send_keys("HP Pavilion azul")
# press enter
textbox.send_keys("\n")

sleep(WAIT_TIME)

# elegir el primer elemento
driver.find_element(
    By.CSS_SELECTOR, ".s-main-slot .s-list-col-right h2 .a-link-normal").click()
sleep(WAIT_TIME)
# cambiar el valor a 2 items
select = Select(driver.find_element(
    By.CSS_SELECTOR, '#desktop_qualifiedBuyBox select'))
select.select_by_value("2")

sleep(WAIT_TIME)

# click en el botón "agregar al carrito"
driver.find_element(
    By.CSS_SELECTOR, "#desktop_qualifiedBuyBox #add-to-cart-button").click()

# verificar el carrito
sleep(WAIT_TIME)
driver.find_element(By.CSS_SELECTOR, "#nav-cart").click()
sleep(3)