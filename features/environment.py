from selenium import webdriver
import os


def before_all(context):
    print(':: Using local webdriver...')
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1280")
    options.add_argument("--start-fullscreen")
    context.browser = webdriver.Chrome(chrome_options=options)


def after_all(context):
    context.browser.quit()
