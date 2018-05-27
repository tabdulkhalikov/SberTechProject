from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def enterRequestInSearchString(context, request):
    input_search = (By.XPATH, '//input[@aria-label="Запрос"]')
    search_btn = (By.XPATH, '//button[@type="submit"]')
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.element_to_be_clickable(input_search)).send_keys(request)
    wait.until(EC.element_to_be_clickable(search_btn)).click()


def selectSite(context, link):
    a = (By.XPATH, "//a[@href='{}']".format(link))
    wait = WebDriverWait(context.browser, 10)
    element = wait.until(EC.element_to_be_clickable(a))
    element.click()


def checkExistItem(context, item):
    WebDriverWait(context.browser, 120).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "%s")]' % item))
    )
    assert context.browser.find_element_by_xpath(By.XPATH, '//*[contains(text(), "%s")]' % item)


#TODO Не работает
def selectSubTabOfMainMenu(context, tab, subtab):
    menu = (By.XPATH, "//button[span='{}']".format(tab))
    hiddenmenu = (By.XPATH, "//li/a[span='{}']".format(subtab))
    actions = ActionChains(context.browser)
    actions.move_to_element(menu)
    actions.click(hiddenmenu)
    actions.perform()


def selectItem(context, item):
    details_btn = (By.CSS_SELECTOR, "a[title='{}']".format(item))
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.element_to_be_clickable(details_btn)).click()


