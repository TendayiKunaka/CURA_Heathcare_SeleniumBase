from seleniumbase import BaseCase
import time
from page_object.home_page import HomePage


class Cura_Health(BaseCase):
    def setUp(self):
        super().setUp()
        print("RUNNING BEFORE EACH TEST")

        # open url * maximize
        self.open(HomePage.url)
        self.maximize_window()

    def tearDown(self):
        print("RUNNING AFTER EACH TEST")
        super().tearDown()

    def test_home(self):
        # assert title
        self.assert_title(HomePage.title)
        # assert copyright
        # self.assert_equal("Copyright © CURA Healthcare Service 2023", HomePage.copyright)
        # assert url
        home_page = self.get_current_url()
        self.assert_equal(HomePage.url, home_page)
        # assert welcome note
        self.assert_text("CURA Healthcare Service", "h1")

    def test_login(self):
        # login
        self.click(HomePage.make_appointment)
        name = self.get_text(HomePage.name)
        print(name)
        password = self.get_text(HomePage.password)
        print(password)
        self.send_keys(HomePage.enter_name, name)
        self.send_keys(HomePage.enter_pass, password)
        time.sleep(2)
        self.click(HomePage.submit)
        new_url = self.get_current_url()
        self.assert_equal(HomePage.appointment_url, new_url)

    def test_make_appointment(self):
        self.click(HomePage.make_appointment)
        name = self.get_text(HomePage.name)
        print(name)
        password = self.get_text(HomePage.password)
        print(password)
        self.send_keys(HomePage.enter_name, name)
        self.send_keys(HomePage.enter_pass, password)
        time.sleep(2)
        self.click(HomePage.submit)
        time.sleep(2)
        self.select_option_by_text(HomePage.hospital, "Seoul CURA Healthcare Center")
        self.click(HomePage.terms)
        self.click(HomePage.radio_button)
        self.send_keys(HomePage.calendar, "12/04/2023")
        self.send_keys(HomePage.textarea, "Good Day, can you please schedule time.")
        time.sleep(2)
        self.click(HomePage.submit_appointment)
        time.sleep(4)
        success_appointment = "Appointment Confirmation"
        self.assert_text(success_appointment, "h2")
