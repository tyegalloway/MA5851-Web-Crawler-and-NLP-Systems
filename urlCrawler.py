# You only need to run the below command once to setup your environment
# You must run them in the same folder as the .py file
# pip install selenium
# pip install pandas

# Using pandas for writing to csv files easily
import pandas as pd
import time

from selenium import webdriver

# This is needed as find_elements_by* is depricated, By is used now
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# How to install chromedriver on Mac
# https://jonathansoma.com/lede/foundations-2017/classes/more-scraping/selenium/

# How to fix security warning on Mac
# https://stackoverflow.com/questions/60362018/macos-catalinav-10-15-3-error-chromedriver-cannot-be-opened-because-the-de

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', options=chrome_options)
defaultTimeout = 30
defaultRetryWaitTime = 0.5

# url = "https://www.tripadvisor.com.au/Hotels-g255060-oa150-Sydney_New_South_Wales-Hotels.html";
url = 'https://www.tripadvisor.com.au/Hotels-g255073-Townsville_Queensland-Hotels.html'

# Creates a DataFrame for urls we can save later
hotels = pd.DataFrame(columns=['url'])
hotels.index.name = "hotelId"

# stores the nextPage to parse
nextPage = url


def timedRetryGetAttribute(element, attribute):
    startTime = time.time()
    finishTime = startTime + defaultTimeout

    firstTime = True

    while time.time() < finishTime:
        try:
            if firstTime == False:
                time.sleep(defaultRetryWaitTime)
            firstTime = False
            attr = element.get_attribute(attribute)
            return attr
        except Exception:
            continue
    return ""


def getHotels(driver):
    hotelsNew = []

    listingTitles = WebDriverWait(driver, defaultTimeout).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "listing_title"))
    )

    for titleElement in listingTitles:
        # Needed to catch exception as some titleElement were null
        try:
            childElements = WebDriverWait(titleElement, defaultTimeout).until(
                EC.presence_of_all_elements_located((By.XPATH, './/*'))
            )
        except TypeError:
            continue
        firstElement = childElements[0]

        hrefValue = timedRetryGetAttribute(firstElement, 'href')

        # Needed to catch exception as some values were null and showing as blank lines in the .csv
        try:
            if len(hrefValue) < 5:
                continue
        except TypeError:
            continue

        # Add the URL into our array that we'll save to CSV later
        hotelsNew.append(hrefValue)

    print(f"Found {len(hotelsNew)} hotels on this page")
    return hotelsNew


def getNextPage(driver, currentPageNumber):
    nextPageNumber = currentPageNumber + 1
    pageNumbersElement = WebDriverWait(driver, defaultTimeout).until(
        EC.presence_of_element_located((By.CLASS_NAME, "pageNumbers"))
    )
    pageNumbersElementChildren = WebDriverWait(pageNumbersElement, defaultTimeout).until(
        EC.presence_of_all_elements_located((By.XPATH, './/*'))
    )

    for child in pageNumbersElementChildren:
        pageNumberAttr = timedRetryGetAttribute(child, 'data-page-number')

        # Needed to catch exception as some values are null, such as "..." option
        try:
            pageNumberAttr = pageNumberAttr + ""
        except TypeError:
            continue

        if int(pageNumberAttr) == nextPageNumber:
            return timedRetryGetAttribute(child, 'href')
    return ""


# This tracks the current page number, useful for keeping track when moving through pages
# perhaps change to currentPageNumber?
currentPageNumber = 1

getPageRetryMax = 5
currentTry = 1

try:
    while nextPage != "":

        if currentTry > getPageRetryMax:
            raise Exception("Failed too many times")

        print(f"Downloading current page: {currentPageNumber}")
        driver.get(nextPage)

        print("Adding hotel URLs")
        hotelsNew = None
        try:
            hotelsNew = getHotels(driver)
        except Exception:
            currentTry = currentTry + 1
            continue

        print("Getting next page link")
        try:
            nextPage = getNextPage(driver, currentPageNumber)
        except Exception:
            currentTry = currentTry + 1
            continue

        for hotelNew in hotelsNew:
            hotels.loc[len(hotels)] = [hotelNew]

        currentPageNumber = currentPageNumber + 1
except Exception:
    print("Failed too many times")
finally:
    print("Saving data to disk")
    hotels.to_csv("hotelUrls.csv", index=True, header=True)
    driver.quit()

print("Program finished")