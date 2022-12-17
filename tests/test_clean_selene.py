import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "a.privalov")
@allure.feature("Issue #68 should be visible")
@allure.story("Clean Selene")
@allure.link("https://github.com", name="Testing")
def test_github():
    browser.open("https://github.com")
    s(".header-search-input").click()
    s(".header-search-input").send_keys("eroshenkoam/allure-example")
    s(".header-search-input").submit()
    s(by.link_text("eroshenkoam/allure-example")).click()
    s("#issues-tab").click()
    s(by.partial_text("#68")).should(be.visible)
