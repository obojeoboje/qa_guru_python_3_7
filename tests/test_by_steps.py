import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag('web')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 'a.privalov')
@allure.feature('Issue #68 should be visible')
@allure.story('Clean Selene')
@allure.link('https://github.com', name='Testing')
def test_github_by_steps():
    with allure.step("Открываем GitHub"):
        browser.open("https://github.com")
    with allure.step("Ищем репозиторий"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("eroshenkoam/allure-example")
        s(".header-search-input").submit()
    with allure.step("Выбираем репозиторий"):
        s(by.link_text("eroshenkoam/allure-example")).click()
    with allure.step("Открываем вкладку Issues"):
        s("#issues-tab").click()
    with allure.step("Проверяем, что на странице есть Issue #68"):
        s(by.partial_text("#68")).should(be.visible)
