import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class PracticeProgram():

    def login(self):
        url = "https://courses.letskodeit.com/"
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(5)

        login_Link = driver.find_element(By.XPATH, "//div[@id='navbar-inverse-collapse']//a[text()='Sign In']")
        login_Link.click()

        email_TextBox = driver.find_element(By.ID, "email")
        email_TextBox.send_keys('samaya2021@gmail.cm')

        password_TextBox = driver.find_element(By.ID, "password")
        password_TextBox.send_keys('python')

        login_Button = driver.find_element(By.XPATH, "//input[@value='Login']")
        login_Button.click()

        allCourses_Tab = driver.find_element(By.XPATH, "//a[text()='ALL COURSES']")
        allCourses_Tab.click()

        search_TextBox = driver.find_element(By.NAME, "course")
        search_TextBox.send_keys('javascript')

        search_Button = driver.find_element(By.CLASS_NAME, "find-course")
        search_Button.click()

        course = driver.find_element(By.XPATH,
                                     "//div[@class='zen-course-title dynamic-text']//h4[contains(text(), 'JavaScript')]")
        course.click()

        enroll_button = driver.find_element(By.XPATH, "//button[text()= 'Enroll in Course']")
        enroll_button.click()

        buy_Button = driver.find_element(By.XPATH, "//div//button//i[1]")

        scroll_Bar = buy_Button.location_once_scrolled_into_view
        print("Location of the element " + str(scroll_Bar))
        driver.execute_script("window.scrollBy(0,100);")

        buy_Button.click()

        driver.execute_script("window.scrollBy(0,-100);")

        message_Text = driver.find_element(By.XPATH,
                                           "//div[@class='cc-payment-outer']//span[text()='Your card number is incomplete.']")
        print(str(message_Text.text))

        driver.execute_script("arguments[0].scrollIntoView(true);", message_Text)

        message = "Your card number is incomplete."

        if message == str(message_Text.text):
            print("Matched")
        else:
            print("Unmatched")

        time.sleep(5)


pp = PracticeProgram()
pp.login()
