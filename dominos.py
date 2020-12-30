from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
import os
import re
# Some versions are incompatible with selenium, try https://ftp.mozilla.org/pub/firefox/releases/30.0/win32/en-US/


class orderDominos:
    def __init__(self, pizzatype, toppingslist, infolist):
        self.pizzatype = pizzatype
        self.toppingslist = toppingslist
        self.toppingslist2 = []
        self.first_name = infolist[0]
        self.last_name = infolist[1]
        self.email = infolist[2]
        self.phone_number = ""
        phone_dummy = infolist[3]
        # reformat phone number to dominos standard
        for i in range(len(phone_dummy)):
            if (i == 0):
                self.phone_number += "("
            self.phone_number += phone_dummy[i]
            if (i == 2):
                self.phone_number += ") "
            if (i == 5):
                self.phone_number += "-"
        # UNCOMMENT BELOW FOR REMOTE, HEADLESS DRIVER
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(
            executable_path=os.environ.get("CHROMEDRIVER_PATH"),
            chrome_options=chrome_options)
        # UNCOMMENT BELOW FOR LOCAL DRIVER
        # self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")

    def click_topping(self, topping):
        # MEATS SECTION
        if (topping == '1'):
            self.loop_click(
                ".//*[contains(text(),'Ham')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")

        elif (topping == '2'):
            self.loop_click(
                ".//*[contains(text(),'Beef')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")

        elif (topping == '3'):
            self.loop_click(
                ".//*[contains(text(),'Salami')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")
        elif (topping == '4'):
            self.loop_click(
                ".//*[contains(text(),'Pepperoni')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")
        elif (topping == '5'):
            self.loop_click(
                ".//*[contains(text(),'Italian Sausage')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")
        elif (topping == '6'):
            self.loop_click(
                ".//*[contains(text(),'Premium Chicken')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")
        elif (topping == '7'):
            self.loop_click(
                ".//*[contains(text(),'Bacon')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")
        elif (topping == '8'):
            self.loop_click(
                ".//*[contains(text(),'Philly Steak')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")
        # NON-MEATS SECTION
        elif (topping == '10'):
            self.loop_click(
                ".//*[contains(text(),'Hot Buffalo Sauce')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")
        elif (topping == '11'):
            self.loop_click(
                ".//*[contains(text(),'Garlic')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")
        elif (topping == '12'):
            self.loop_click(
                ".//*[contains(text(),'Jalapeno Peppers')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")
        elif (topping == '13'):
            self.loop_click(
                ".//*[contains(text(),'Onions')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")
        elif (topping == '14'):
            self.loop_click(
                ".//*[contains(text(),'Banana Peppers')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")
        elif (topping == '15'):
            self.loop_click(
                ".//*[contains(text(),'Diced Tomatoes')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")
        elif (topping == '16'):
            self.loop_click(
                ".//*[contains(text(),'Black Olives')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")
        elif (topping == '17'):
            self.loop_click(
                ".//*[contains(text(),'Mushrooms')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")
        elif (topping == '18'):
            self.loop_click(
                ".//*[contains(text(),'Pineapple')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")
        elif (topping == '19'):
            self.loop_click(
                ".//*[contains(text(),'Shredded Provolone Cheese')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")
        elif (topping == '20'):
            self.loop_click(
                ".//*[contains(text(),'Cheddar Cheese')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")
        elif (topping == '21'):
            self.loop_click(
                ".//*[contains(text(),'Green Peppers')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")
        elif (topping == '22'):
            self.loop_click(
                ".//*[contains(text(),'Spinach')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")
        elif (topping == '23'):
            self.loop_click(
                ".//*[contains(text(),'Roasted Red Peppers')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")
        elif (topping == '24'):
            self.loop_click(
                ".//*[contains(text(),'Feta Cheese')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")
        elif (topping == '25'):
            self.loop_click(
                ".//*[contains(text(),'Shredded Parmesan Asiago')]/preceding-sibling::input[@type='checkbox']",
                "XPATH")

    # Function to select toppings for pizza
    def select_toppings(self):
        if (self.pizzatype == 'single'):
            for topping in self.toppingslist:
                self.click_topping(topping)

        elif self.pizzatype == 'double':
            self.click_topping(self.toppingslist[len(self.toppingslist) - 1])
            self.toppingslist.pop()
            self.click_topping(self.toppingslist[len(self.toppingslist) - 1])
            self.toppingslist.pop()

    def find_nearest_store(self):
        # Request Dominos
        self.driver.get(
            "https://www.dominos.com/en/pages/order/?locations=1#/locations/")
        self.driver.implicitly_wait(20)  # Allow page loading

        # Enter Address Information (Type: Apartment)
        Type = self.driver.find_element_by_id("Address_Type_Select")
        for option in Type.find_elements_by_tag_name("option"):
            if option.text == "House":
                option.click()
                break
                # Fill information out prior to use

        # clear autofill garbage
        self.driver.find_element_by_id("Street").clear()  # <--- Street
        self.driver.find_element_by_id(
            "Address_Line_2").clear()  # <--- Apartment
        self.driver.find_element_by_id("City_Sep").clear()
        self.driver.find_element_by_id("Postal_Code_Sep").clear()
        self.driver.find_element_by_id("Street").send_keys(
            "3116 Noriega St")  # <--- Street
        self.driver.find_element_by_id("Address_Line_2").send_keys(
            "")  # <--- Apartment
        self.driver.find_element_by_id("City_Sep").send_keys(
            "San Francisco")  # <--- City
        self.driver.find_element_by_id("Postal_Code_Sep").send_keys(
            "94122")  # <--- Zip

        State = self.driver.find_element_by_id("Region")
        for option in State.find_elements_by_tag_name("option"):
            if option.text == "MI":  # <--- State (Ex. MA, NJ, NY)
                option.click()
                break

        # Search for locations
        self.loop_click(".//*[@id='locationSearchForm']/div/div[4]/button",
                        "XPATH")
        # self.driver.find_element(
        #     By.XPATH,
        #     ".//*[@id='locationSearchForm']/div/div[4]/button").click()
        self.driver.implicitly_wait(20)  # Allow page loading

        # Click store pickup for closest store
        self.loop_click(
            ".//*[@id='locationsResultsPage']/div[4]/div[2]/div[1]/div[2]/div/div[2]/div[1]/a",
            "XPATH")
        # self.driver.find_element(
        #     By.XPATH,
        #     ".//*[@id='locationsResultsPage']/div[4]/div[2]/div[1]/div[2]/div/div[2]/div[1]/a"
        # ).click()
        self.driver.implicitly_wait(20)  # Allow page loading

    def get_single(self):
        #Get to Pizza Ordering Screen
        self.driver.get(
            "https://www.dominos.com/en/pages/order/#/product/S_PIZZA/builder/"
        )

        #Skip to Toppings Page
        self.loop_click(".//*[@id='toppings']", "XPATH")
        # self.driver.find_element_by_xpath(".//*[@id='toppings']").click()
        # Click "No Thanks" button
        # Below fixes the not clickable at this point error.
        self.loop_click(".//*[@id='stepUpsell']/div/button[1]", "XPATH")

        # self.driver.execute_script(
        #     "arguments[0].click();",
        #     WebDriverWait(self.driver, 20).until(
        #         EC.element_to_be_clickable(
        #             (By.XPATH, ".//*[@id='stepUpsell']/div/button[1]"))))
        self.driver.implicitly_wait(20)  # Allow page loading

        # ADD INGREDIENTS SECTION
        self.select_toppings()
        self.driver.implicitly_wait(20)  # Allow page loading

        #Click "Add to Order" button
        self.loop_click(
            ".//*[@id='pizzaSummaryInColumn']/div[1]/div[2]/div[2]/button",
            "XPATH")
        # self.driver.find_element_by_xpath(
        #     ".//*[@id='pizzaSummaryInColumn']/div[1]/div[2]/div[2]/button"
        # ).click()
        self.driver.implicitly_wait(20)  # Allow page loading

        # navigate to coupons page
        self.driver.get(
            "https://www.dominos.com/en/pages/order/#!/section/Coupons/category/All/"
        )
        self.driver.refresh()
        # click "Add Coupon" button
        self.loop_click(
            "(//*[contains(text(),'$7.99')])[1]/parent::*/preceding-sibling::*//*",
            "XPATH")

        # Click "Done With This Coupon" Button
        self.loop_click(
            ".//*[@id='genericOverlay']/section/div/div[6]/div[2]/a", "XPATH")
        self.driver.implicitly_wait(20)  # Allow page loading

        # Click "Continue Checkout" Button
        # loop_click(".//*[@id='js-myOrderPage']/a")
        # self.driver.get('https://www.dominos.com')

    def get_double(self):
        for i in range(2):
            #Get to Pizza Ordering Screen
            self.driver.get(
                "https://www.dominos.com/en/pages/order/#/product/S_PIZZA/builder/"
            )

            #Skip to Toppings Page
            self.driver.find_element_by_id("pizza_size|12").click()

            self.loop_click(".//*[@id='toppings']", "XPATH")
            # self.driver.find_element_by_xpath(".//*[@id='toppings']").click()
            self.driver.implicitly_wait(20)  # Allow page loading
            # self.driver.find_element_by_id("pizza_size|12").click()
            # self.driver.find_element_by_id("pizza_size|12").click()
            if (i == 0):
                # Click "No Thanks" button
                # Below fixes the not clickable at this point error.
                self.loop_click(".//*[@id='stepUpsell']/div/button[1]",
                                "XPATH")
                # self.driver.execute_script(
                #     "arguments[0].click();",
                #     WebDriverWait(self.driver, 20).until(
                #         EC.element_to_be_clickable(
                #             (By.XPATH,
                #              ".//*[@id='stepUpsell']/div/button[1]"))))
            self.driver.implicitly_wait(20)  # Allow page loading

            # ADD INGREDIENTS SECTION
            self.select_toppings()
            self.driver.implicitly_wait(20)  # Allow page loading

            #Click "Add to Order" button
            self.loop_click(
                ".//*[@id='pizzaSummaryInColumn']/div[1]/div[2]/div[2]/button",
                "XPATH")
            # self.driver.find_element_by_xpath(
            #     ".//*[@id='pizzaSummaryInColumn']/div[1]/div[2]/div[2]/button"
            # ).click()

            self.driver.refresh()

        self.driver.implicitly_wait(20)  # Allow page loading

        self.driver.get(
            "https://www.dominos.com/en/pages/order/coupon#!/coupon/national/")
        self.driver.implicitly_wait(100)  # Allow page loading

        # self.driver.find_element_by_class_name(
        #     "featured-coupon-599MixMatch").click()
        self.loop_click("featured-coupon-599MixMatch", "CLASS_NAME")

        # Click "Done With This Coupon" Button
        self.loop_click(
            ".//*[@id='genericOverlay']/section/div/div[6]/div[2]/a", "XPATH")
        self.driver.get('https://www.dominos.com')

    def checkout(self):
        # Straight to checkout
        self.driver.get("https://www.dominos.com/en/pages/order/payment.jsp")
        # Enter contact information
        self.driver.find_element_by_id("First_Name").send_keys(
            self.first_name)  # <--- First Name
        self.driver.find_element_by_id("Last_Name").send_keys(
            self.last_name)  # <--- Last Name
        self.driver.find_element_by_id("Email").send_keys(
            self.email)  # <--- Email
        self.driver.find_element_by_id("Callback_Phone").clear()
        self.driver.find_element_by_id("Callback_Phone").send_keys(
            self.phone_number)  # <--- Phone

        results = self.driver.find_elements(
            By.CSS_SELECTOR, "li[data-quid='topping-part-Whole:']")
        total = self.driver.find_element(
            By.CSS_SELECTOR,
            ".finalizedTotal.js-total").get_attribute("innerHTML")
        dummy_string = ""
        for r in results:
            dummy_string += r.get_attribute("innerHTML")
        toppings_clicked = re.findall("\w*[',']\s\s\w*", dummy_string)
        return {'total': str(total), 'toppings': str(toppings_clicked)}

    def complete_order(self):
        total = self.driver.find_element(
            By.CSS_SELECTOR,
            ".finalizedTotal.js-total").get_attribute("innerHTML")
        print(total)

    def order_pizza(self):
        self.find_nearest_store()
        if (self.pizzatype == 'single'):
            self.get_single()
        elif (self.pizzatype == 'double'):
            self.get_double()
        self.checkout()

    # loop_click and wait until element is clickable by Selenium
    def loop_click(self, string, by):
        max_attempts = 3
        attempt = 1
        while True:
            try:
                if (by == "XPATH"):
                    self.driver.execute_script(
                        "arguments[0].click();",
                        WebDriverWait(self.driver, 50).until(
                            EC.element_to_be_clickable((By.XPATH, string))))
                    break
                elif (by == "CLASS_NAME"):
                    self.driver.execute_script(
                        "arguments[0].click();",
                        WebDriverWait(self.driver, 50).until(
                            EC.element_to_be_clickable(
                                (By.CLASS_NAME, string))))
                    break
                elif (by == "ID"):
                    self.driver.execute_script(
                        "arguments[0].click();",
                        WebDriverWait(self.driver, 50).until(
                            EC.element_to_be_clickable((By.ID, string))))
                    break

            except StaleElementReferenceException:
                if attempt == max_attempts:
                    raise
                attempt += 1

    def loop_click_id(self, string, max_attempts=3):
        attempt = 1
        while True:
            try:
                self.driver.execute_script(
                    "arguments[0].click();",
                    WebDriverWait(self.driver, 50).until(
                        EC.element_to_be_clickable((By.XPATH, string))))
                break
            except StaleElementReferenceException:
                if attempt == max_attempts:
                    raise
                attempt += 1

    # loop_click and wait until element is clickable by Selenium
    # def loop_click(self, string, max_attempts=3):
    #     attempt = 1
    #     while True:
    #         try:
    #             self.driver.execute_script(
    #                 "arguments[0].click();",
    #                 WebDriverWait(self.driver, 50).until(
    #                     EC.element_to_be_clickable((By.CLASS_NAME, string))))
    #             break
    #         except StaleElementReferenceException:
    #             if attempt == max_attempts:
    #                 raise
    #             attempt += 1

    # def loop_click_id(self, string, max_attempts=3):
    #     attempt = 1
    #     while True:
    #         try:
    #             self.driver.execute_script(
    #                 "arguments[0].click();",
    #                 WebDriverWait(self.driver, 50).until(
    #                     EC.element_to_be_clickable((By.ID, string))))
    #             break
    #         except StaleElementReferenceException:
    #             if attempt == max_attempts:
    #                 raise
    #             attempt += 1


# pizzaobj = orderDominos("double", ["1", "2", "3", "4"],
#                         ["ya", "no", "yano@gmail.com", "2345678910"])
# pizzaobj.order_pizza()
# pizzaobj2 = orderDominos("single", ["1", "2", "3"],
#                          ["ya", "no", "yano@gmail.com", "2345678910"])
# pizzaobj2.order_pizza()