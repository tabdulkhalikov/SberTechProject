from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def enterRequestInSearchString(context, request):
    a = (By.XPATH, '//input[@aria-label="Запрос"]')
    wait = WebDriverWait(context.browser, 10)
    element = wait.until(EC.element_to_be_clickable(a))
    element.send_keys(request)


def pushToSubmitButton(context):
    a = (By.XPATH, '//button[@type="submit"]')
    wait = WebDriverWait(context.browser, 10)
    element = wait.until(EC.element_to_be_clickable(a))
    element.click()

# TODO не стабильный
def selectLink(context, link):
    a = (By.XPATH, "//a[@href='{}']".format(link))
    wait = WebDriverWait(context.browser, 10)
    element = wait.until(EC.element_to_be_clickable(a))
    element.click()


def checkExistItem(context, item):
    a = (By.XPATH, "//h5[a='{}']".format(item))
    wait = WebDriverWait(context.browser, 10)
    isExist = EC.element_to_be_clickable(a)
    return isExist

#TODO Разобраться
def selectTabOfMainMenu(context, tab):
    tab = context.browser.find_element_by_xpa(".nav")
    hidden_submenu = (By.XPATH, "//li[@class='nav-2-5']")
    actions = ActionChains(context.browser)
    actions.move_to_element(tab)
    actions.click(hidden_submenu)
    actions.perform()
