import pytest

import config
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright

import pytest

from pages.base_page import BasePage
from pages.main_tires_page import MainTiresPage


@pytest.fixture
def page():  # Изменение типа возвращаемого значения
    playwright = sync_playwright().start()
    browser = get_chrome_browser(playwright)
    context = get_context(browser)
    page = context.new_page()
    # Создаем экземпляр CheqPage
    yield page  # Возвращаем cheq_page вместо page_data
    for context in browser.contexts:
        context.close()
    browser.close()
    playwright.stop()


@pytest.fixture
def main_page(page):
    return MainTiresPage(page)


@pytest.fixture
def base_page(page):
    return BasePage(page)


def get_chrome_browser(playwright) -> Browser:
    return playwright.chromium.launch(
        headless=config.playwright.IS_HEADLESS,
        slow_mo=config.playwright.SLOW_MO
    )


def get_context(browser) -> BrowserContext:
    context = browser.new_context(
        viewport=config.playwright.PAGE_VIEWPORT_SIZE,
    )
    context.set_default_timeout(
        timeout=config.expectations.DEFAULT_TIMEOUT
    )
    return context
