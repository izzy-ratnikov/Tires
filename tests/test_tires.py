import time
from playwright.sync_api import expect
import pytest

from config import Url
from pages.main_tires_page import MainTiresPage


class TestTires:
    # def test_form_with_correct_information(self, main_page):
    #     main_page.open_tires_site()
    #     main_page.type_of_tire_form()
    #     main_page.icvc_form()
    #     main_page.diameter_form()
    #     main_page.season_form()
    #     main_page.width_form()
    #     main_page.profile_form()
    #     main_page.manufacturer_form()
    #     main_page.url_form()
    #     main_page.urls_form()
    #     main_page.information_form()
    #     # main_page.in_archive_button()
    #     main_page.price_form()
    #     main_page.submit_button()
    #     time.sleep(2)

    def test_width(self, main_page):
        main_page.open_tires_site()
        main_page.choose_tires_by_width()

    def test_profile(self, main_page):
        main_page.open_tires_site()
        main_page.choose_profile()

    def test_diametr(self, main_page):
        main_page.open_tires_site()
        main_page.choose_diametr()

    def test_season(self, main_page):
        main_page.open_tires_site()
        main_page.choose_season()

    def test_choose_manufacture_premium(self, main_page):
        main_page.open_tires_site()
        main_page.choose_manufacture_premium()

    def test_all_manufactures(self, main_page):
        main_page.open_tires_site()
        main_page.choose_all_manufactures()
