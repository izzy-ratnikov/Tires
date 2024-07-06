import time

from playwright.sync_api import Page
import config

from pages.base_page import BasePage


class MainTiresPage(BasePage):
    CHOOSE_WIDTH = '#width'
    CHOOSE_PROFILE = 'div.choose-profile > select'
    BUTTON = '.btn-wrapper'
    CARD = '.card'
    MANUFACTURE = '.choose-manufacturer'
    CLAS_PREMIUM = '#premium'
    CLAS_MEDIUM = '#medium'
    CLAS_ECONOM = '#ekonomiczna'
    CHOOSE_CLAS = '//*[@id="root"]//div[4]/button'
    CHOOSE_DIAMETR = 'div.choose-diametr > select'
    CHOOSE_SEASON = 'div.choose-season > select'

    # TYPE_OF_TIRE_FORM = '//*[@id="input1"]'
    # ICVC_FROM = '//*[@id="input2"]'
    # DIAMETER_FORM = '//*[@id="input3"]'
    # SEASON_FORM = '//*[@id="input11"]'
    # WIDTH_FORM = '//*[@id="input4"]'
    # PROFILE_FORM = '//*[@id="input5"]'
    # MANUFACTURER_FORM = '//*[@id="input6"]'
    # URL_FORM = '//*[@id="input7"]'
    # URLS_FORM = '//*[@id="input8"]'
    # INFORMATION_FORM = '//*[@id="input9"]'
    # IN_ARCHIVE_BUTTON = '//*[@id="input10"]'
    # PRICE_FORM = '//*[@id="input12"]'
    # BUTTON_SUBMIT_FORM = '//*[@id="content"]//div[13]/input'

    # def open_tires_site(self) -> None:
    #     self.page.goto(config.url.TIRES_DOMEN)
    #
    # def type_of_tire_form(self):
    #     self.page.locator(self.TYPE_OF_TIRE_FORM).click()
    #     self.page.locator(self.TYPE_OF_TIRE_FORM).fill("")
    #
    # def icvc_form(self):
    #     self.page.locator(self.ICVC_FROM).click()
    #     self.page.locator(self.ICVC_FROM).fill("001")
    #
    # def diameter_form(self):
    #     self.page.locator(self.DIAMETER_FORM).click()
    #     self.page.locator(self.DIAMETER_FORM).fill("29")
    #
    # def season_form(self):
    #     self.page.locator(self.SEASON_FORM).click()
    #     self.page.locator(self.SEASON_FORM).fill("52")
    #
    # def width_form(self):
    #     self.page.locator(self.WIDTH_FORM).click()
    #     self.page.locator(self.WIDTH_FORM).fill("198")
    #
    # def profile_form(self):
    #     self.page.locator(self.PROFILE_FORM).click()
    #     self.page.locator(self.PROFILE_FORM).fill("30")
    #
    # def manufacturer_form(self):
    #     self.page.locator(self.MANUFACTURER_FORM).click()
    #     self.page.locator(self.MANUFACTURER_FORM).fill("111")
    #
    # def url_form(self):
    #     self.page.locator(self.URL_FORM).click()
    #     self.page.locator(self.URL_FORM).fill("")
    #
    # def urls_form(self):
    #     self.page.locator(self.URLS_FORM).click()
    #     self.page.locator(self.URLS_FORM).fill("")
    #
    # def information_form(self):
    #     self.page.locator(self.INFORMATION_FORM).click()
    #     self.page.locator(self.INFORMATION_FORM).fill("")
    #
    # def in_archive_button(self):
    #     self.page.locator(self.IN_ARCHIVE_BUTTON).click()
    #
    # def price_form(self):
    #     self.page.locator(self.PRICE_FORM).click()
    #     self.page.locator(self.PRICE_FORM).fill("52")
    #
    # def submit_button(self):
    #     self.page.locator(self.BUTTON_SUBMIT_FORM).click()

    def open_tires_site(self) -> None:
        self.page.goto(config.url.TIRES_URL)

    def choose_tires_by_width(self):
        self.page.select_option(self.CHOOSE_WIDTH, value='30')
        self.page.locator(self.BUTTON).click()
        self.is_element_visible(self.CARD)
        self.to_have_count(self.CARD, 1)

    def choose_profile(self):
        c_p = self.page.locator(self.CHOOSE_PROFILE)
        c_p.select_option('65')
        self.page.locator(self.BUTTON).click()
        self.is_element_visible(self.CARD)
        self.to_have_count(self.CARD, 1)

    def choose_diametr(self):
        c_d = self.page.locator(self.CHOOSE_DIAMETR)
        c_d.select_option('18')
        self.page.locator(self.BUTTON).click()
        self.is_element_visible(self.CARD)
        self.to_have_count(self.CARD, 1)

    def choose_season(self):
        c_s = self.page.locator(self.CHOOSE_SEASON)
        c_s.select_option('winter')
        self.page.locator(self.BUTTON).click()
        self.is_element_visible(self.CARD)
        self.to_have_count(self.CARD, 1)

    def choose_manufacture_premium(self):
        self.page.locator(self.MANUFACTURE).click()
        self.page.locator(self.CLAS_PREMIUM).click()
        self.page.locator(self.CHOOSE_CLAS).click()
        self.page.locator(self.BUTTON).click()
        self.to_have_count(self.CARD, 9)

    def choose_all_manufactures(self):
        self.page.locator(self.MANUFACTURE).click()
        self.page.locator(self.CLAS_PREMIUM).click()
        self.page.locator(self.CLAS_MEDIUM).click()
        self.page.locator(self.CLAS_ECONOM).click()
        self.page.locator(self.CHOOSE_CLAS).click()
        self.page.locator(self.BUTTON).click()
        self.to_have_count(self.CARD, 27)