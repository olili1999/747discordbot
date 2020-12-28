from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="./chromedriver.exe")

# Some versions are incompatible with selenium, try https://ftp.mozilla.org/pub/firefox/releases/30.0/win32/en-US/

# Request Dominos
driver.get("https://www.dominos.com/en/pages/order/?locations=1#/locations/")
driver.implicitly_wait(5)  # Allow page loading

# Enter Address Information (Type: Apartment)
Type = driver.find_element_by_id("Address_Type_Select")
for option in Type.find_elements_by_tag_name("option"):
    if option.text == "House":
        option.click()
        break
        # Fill information out prior to use

# clear autofill garbage
driver.find_element_by_id("Street").clear()  # <--- Street
driver.find_element_by_id("Address_Line_2").clear()  # <--- Apartment
driver.find_element_by_id("City_Sep").clear()
driver.find_element_by_id("Postal_Code_Sep").clear()

driver.find_element_by_id("Street").send_keys("3116 Noriega St")  # <--- Street
driver.find_element_by_id("Address_Line_2").send_keys("")  # <--- Apartment
driver.find_element_by_id("City_Sep").send_keys("San Francisco")  # <--- City
driver.find_element_by_id("Postal_Code_Sep").send_keys("94122")  # <--- Zip

State = driver.find_element_by_id("Region")
for option in State.find_elements_by_tag_name("option"):
    if option.text == "MI":  # <--- State (Ex. MA, NJ, NY)
        option.click()
        break

# Search for locations
driver.find_element(
    By.XPATH, ".//*[@id='locationSearchForm']/div/div[4]/button").click()
driver.implicitly_wait(10)  # Allow page loading

# click store pickup for nearby store
driver.find_element(
    By.XPATH,
    ".//*[@id='locationsResultsPage']/div[4]/div[2]/div[1]/div[2]/div/div[2]/div[1]/a"
).click()

single = False
double = True
driver.implicitly_wait(10)  # Allow page loading


def loop(string, max_attempts=3):
    attempt = 1
    while True:
        try:
            driver.execute_script(
                "arguments[0].click();",
                WebDriverWait(driver, 50).until(
                    EC.element_to_be_clickable((By.XPATH, string))))
            break
        except StaleElementReferenceException:
            if attempt == max_attempts:
                raise
            attempt += 1


def select_toppings(toppings):
    for topping in toppings:
        if (topping == '1'):
            loop(
                ".//*[contains(text(),'Ham')]/preceding-sibling::input[@type='checkbox']"
            )

        elif (topping == '2'):
            loop(
                ".//*[contains(text(),'Beef')]/preceding-sibling::input[@type='checkbox']"
            )

        elif (topping == '3'):
            loop(
                ".//*[contains(text(),'Salami')]/preceding-sibling::input[@type='checkbox']"
            )
        elif (topping == '4'):
            loop(
                ".//*[contains(text(),'Pepperoni')]/preceding-sibling::input[@type='checkbox']"
            )
        elif (topping == '5'):
            loop(
                ".//*[contains(text(),'Italian Sausage')]/preceding-sibling::input[@type='checkbox']"
            )
        elif (topping == '6'):
            loop(
                ".//*[contains(text(),'Premium Chicken')]/preceding-sibling::input[@type='checkbox']"
            )
        elif (topping == '7'):
            loop(
                ".//*[contains(text(),'Bacon')]/preceding-sibling::input[@type='checkbox']"
            )
        elif (topping == '8'):
            loop(
                ".//*[contains(text(),'Philly Steak')]/preceding-sibling::input[@type='checkbox']"
            )
        elif (topping == '10'):
            loop(
                ".//*[contains(text(),'Hot Buffalo Sauce')]/preceding-sibling::input[@type='checkbox']"
            )
        elif (topping == '11'):
            loop(
                ".//*[contains(text(),'Garlic')]/preceding-sibling::input[@type='checkbox']"
            )
        elif (topping == '12'):
            loop(
                ".//*[contains(text(),'Jalapeno Peppers')]/preceding-sibling::input[@type='checkbox']"
            )
        elif (topping == '13'):
            loop(
                ".//*[contains(text(),'Onions')]/preceding-sibling::input[@type='checkbox']"
            )
        elif (topping == '14'):
            loop(
                ".//*[contains(text(),'Banana Peppers')]/preceding-sibling::input[@type='checkbox']"
            )
        elif (topping == '15'):
            loop(
                ".//*[contains(text(),'Diced Tomatoes')]/preceding-sibling::input[@type='checkbox']"
            )
        elif (topping == '16'):
            loop(
                ".//*[contains(text(),'Black Olives')]/preceding-sibling::input[@type='checkbox']"
            )
        elif (topping == '17'):
            loop(
                ".//*[contains(text(),'Mushrooms')]/preceding-sibling::input[@type='checkbox']"
            )
        elif (topping == '18'):
            loop(
                ".//*[contains(text(),'Pineapple')]/preceding-sibling::input[@type='checkbox']"
            )
        elif (topping == '19'):
            loop(
                ".//*[contains(text(),'Shredded Provolone Cheese')]/preceding-sibling::input[@type='checkbox']"
            )
        elif (topping == '20'):
            loop(
                ".//*[contains(text(),'Cheddar Cheese')]/preceding-sibling::input[@type='checkbox']"
            )
        elif (topping == '21'):
            loop(
                ".//*[contains(text(),'Green Peppers')]/preceding-sibling::input[@type='checkbox']"
            )
        elif (topping == '22'):
            loop(
                ".//*[contains(text(),'Spinach')]/preceding-sibling::input[@type='checkbox']"
            )
        elif (topping == '23'):
            loop(
                ".//*[contains(text(),'Roasted Red Peppers')]/preceding-sibling::input[@type='checkbox']"
            )
        elif (topping == '24'):
            loop(
                ".//*[contains(text(),'Feta Cheese')]/preceding-sibling::input[@type='checkbox']"
            )
        elif (topping == '25'):
            loop(
                ".//*[contains(text(),'Shredded Parmesan Asiago')]/preceding-sibling::input[@type='checkbox']"
            )


if (single == True):
    #Get to Pizza Ordering Screen
    driver.get(
        "https://www.dominos.com/en/pages/order/#/product/S_PIZZA/builder/")

    #Skip to Toppings Page
    driver.find_element_by_xpath(".//*[@id='toppings']").click()
    # Click "No Thanks" button
    # Below fixes the not clickable at this point error.
    driver.execute_script(
        "arguments[0].click();",
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, ".//*[@id='stepUpsell']/div/button[1]"))))
    driver.implicitly_wait(20)  # Allow page loading

    # ADD INGREDIENTS SECTION
    loop(
        ".//*[contains(text(),'Ham')]/preceding-sibling::input[@type='checkbox']"
    )

    loop(
        ".//*[contains(text(),'Italian Sausage')]/preceding-sibling::input[@type='checkbox']"
    )
    loop(
        ".//*[contains(text(),'Bacon')]/preceding-sibling::input[@type='checkbox']"
    )

    #Click "Add to Order" button
    driver.find_element_by_xpath(
        ".//*[@id='pizzaSummaryInColumn']/div[1]/div[2]/div[2]/button").click(
        )
    # navigate to coupons page
    driver.get(
        "https://www.dominos.com/en/pages/order/#!/section/Coupons/category/All/"
    )
    driver.refresh()
    # click "Add Coupon" button
    driver.execute_script(
        "arguments[0].click();",
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "(//*[contains(text(),'$7.99')])[1]/parent::*/preceding-sibling::*//*"
            ))))

    # Click "Done With This Coupon" Button
    loop(".//*[@id='genericOverlay']/section/div/div[6]/div[2]/a")

    # Click "Continue Checkout" Button
    # loop(".//*[@id='js-myOrderPage']/a")
    driver.get('https://www.dominos.com')

if (double == True):
    for i in range(2):
        #Get to Pizza Ordering Screen
        driver.get(
            "https://www.dominos.com/en/pages/order/#/product/S_PIZZA/builder/"
        )

        #Skip to Toppings Page
        driver.find_element_by_xpath(".//*[@id='toppings']").click()
        driver.find_element_by_id("pizza_size|12").click()
        if (i == 0):
            # Click "No Thanks" button
            # Below fixes the not clickable at this point error.
            driver.execute_script(
                "arguments[0].click();",
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable(
                        (By.XPATH, ".//*[@id='stepUpsell']/div/button[1]"))))
        driver.implicitly_wait(20)  # Allow page loading

        # ADD INGREDIENTS SECTION
        loop(
            ".//*[contains(text(),'Ham')]/preceding-sibling::input[@type='checkbox']"
        )

        loop(
            ".//*[contains(text(),'Italian Sausage')]/preceding-sibling::input[@type='checkbox']"
        )

        #Click "Add to Order" button
        driver.find_element_by_xpath(
            ".//*[@id='pizzaSummaryInColumn']/div[1]/div[2]/div[2]/button"
        ).click()

        driver.refresh()

    driver.implicitly_wait(20)  # Allow page loading

    driver.get(
        "https://www.dominos.com/en/pages/order/coupon#!/coupon/national/")
    driver.implicitly_wait(100)  # Allow page loading

    driver.find_element_by_class_name("featured-coupon-599MixMatch").click()

    # Click "Done With This Coupon" Button
    loop(".//*[@id='genericOverlay']/section/div/div[6]/div[2]/a")
    driver.get('https://www.dominos.com')

# Straight to checkout
# driver.get("https://www.dominos.com/en/pages/order/payment.jsp")
# # Enter contact information
# driver.find_element_by_id("First_Name").send_keys("Oliver")  # <--- First Name
# driver.find_element_by_id("Last_Name").send_keys("Li")  # <--- Last Name
# driver.find_element_by_id("Email").send_keys("olili@umich.edu")  # <--- Email
# driver.find_element_by_id("Callback_Phone").clear()
# driver.find_element_by_id("Callback_Phone").send_keys(
#     "(248) 495-3497")  # <--- Phone
# coupon code 9133
# https://www.dominos.com/en/pages/order/#/product/S_PIZZA/builder/?couponCode=9193&code=12SCREEN