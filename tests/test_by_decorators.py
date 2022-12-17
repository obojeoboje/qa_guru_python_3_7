import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'a.privalov')
@allure.feature('Issue #68 should be visible')
@allure.story('Clean Selene')
@allure.link('https://github.com', name='Testing')
def test_github_by_decorators():
    open_main_page()
    find_repo('eroshenkoam/allure-example')
    open_repo('eroshenkoam/allure-example')
    open_issue()
    check_repo_with_number('#68')


@allure.step('Открываем GitHub')
def open_main_page():
    browser.open('https://github.com/')


@allure.step('Ищем репозиторий {repository}')
def find_repo(repository):
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').type(repository)
    browser.element('.header-search-input').press_enter()


@allure.step('Выбираем репозиторий {repository}')
def open_repo(repository):
    browser.element(by.link_text(repository)).click()


@allure.step('Открываем вкладку Issues')
def open_issue():
    browser.element('#issues-tab').click()


@allure.step('Проверяем, что на странице есть Issue {num}')
def check_repo_with_number(num):
    browser.element(by.partial_text(num)).should(be.visible)


browser.quit()
