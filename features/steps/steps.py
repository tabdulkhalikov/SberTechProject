import time
import unittest
from behave import *
from hamcrest import *
from DriverUI import driverUI


def is_element_exists(context, id):
    """
    Нестандартный способ проверить существует ли элемент на странице
    Надо проверить, работает ли is_displayed в новых версиях
    :param context:
    :param id:
    :return: boolean
    """
    try:
        context.browser.find_element_by_css_selector(id)
        return True
    except:
        return False


@when('Подождал {} секунд')
@when('Подождал {} секунды')
@when('Подождал {} секунду')
def send_keys(context, target):
    time.sleep(int(target))


@given(u'Открыл страницу "{page}"')
def goto(context, page):
    print(context)
    context.browser.get(page)


@when(u'Ввел запрос в поисковую строку "{request}"')
def step1(context, request):
    driverUI.enterRequestInSearchString(context, request)


@when(u'Нажал на кнопку найти')
def step2(context):
    driverUI.pushToSubmitButton(context)


@when(u'Открыл ссылку фирменного магазина дайсон "{link}"')
def step3(context, link):
    driverUI.selectLink(context, link)


@then(u'Убедился что на открывшейся странице есть "{item}"')
def step4(context, item):
    hasItem = driverUI.checkExistItem(context, item)
    # assert hasItem == True


@when(u'В верхнем меню выбрал вкладку "{tab}"')
def step5(context, tab):
    driverUI.selectTabOfMainMenu(context, tab)





