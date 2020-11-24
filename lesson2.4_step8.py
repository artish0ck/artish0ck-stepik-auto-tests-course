from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")


    # говорим Selenium проверять в течение 5 секунд, пока цена не станет 100$



    price = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    book = browser.find_element_by_id("book")
    book.click()


    x_value = browser.find_element_by_id("input_value")
    x = x_value.text
    result = math.log(abs(12*math.sin(int(x))))

    text_area = browser.find_element_by_id("answer")
    text_area.send_keys(str(result))
    print(type(result))

    submit = browser.find_element_by_id("solve")
    submit.click() 

finally:
    time.sleep(15)
    browser.quit()





