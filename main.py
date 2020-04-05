from selenium.webdriver import Chrome, ChromeOptions
from selenium.common.exceptions import NoSuchElementException

### NOTE: Please change this according to your environment
EXECUTABLE_PATH_GOOGLE_CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
EXECUTABLE_PATH_GOOGLE_CHROME_DRIVER = "./chromedriver"

### Initialize webdriver
options = ChromeOptions()
options.binary_location = EXECUTABLE_PATH_GOOGLE_CHROME
driver_location = EXECUTABLE_PATH_GOOGLE_CHROME_DRIVER
webdriver = Chrome(driver_location, options=options)

### Scraping process
url = "https://play.google.com/store/apps/details?id=com.lazada.android&hl=en&showAllReviews=true"

# Webdriver get the URL
webdriver.get(url)

# Webdriver get all review elements
elements = webdriver.find_elements_by_css_selector("div[jscontroller='H6eOGe']")
for element in elements:
    element_name = element.find_element_by_class_name("X43Kjb")
    name = element_name.text

    element_rate = element.find_element_by_class_name("pf5lIe").find_element_by_tag_name("div")
    rate = element_rate.get_attribute("aria-label")

    element_date = element.find_element_by_class_name("p2TkOb")
    date = element_date.text

    element_liked_by = element.find_element_by_class_name("jUL89d")
    liked_by = element_liked_by.text if element_liked_by.text != "" else "0"

    # If there is full-review button, click it first to load get complete review
    element_review = element.find_element_by_class_name("UD7Dzf")
    try:
        element_review.find_element_by_tag_name("button").click()
    except NoSuchElementException:
        pass
    review = element_review.text

    print(name)
    print(rate)
    print(date)
    print(liked_by)
    print(review)