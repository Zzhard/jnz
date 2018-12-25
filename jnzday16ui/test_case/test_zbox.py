'''

这里写业务的用例
用例要用到
    page
    unittest


'''
from page.basePage import Page
import unittest


class UiTester(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = Page()
        cls.page.open()

    def test_a_login(self):
        self.page.send_username()
        self.page.send_passwd()
        self.page.login()
        self.assertTrue(self.page.check_login())

    def test_b_createBug(self):
        self.page.click_bug()
        self.page.crt_bug()
        self.page.module()
        self.page.version()
        self.page.type()
        self.page.os()
        self.page.browser()
        self.page.date()
        self.page.title()
        self.page.content()
        self.page.save()
        self.assertTrue(self.page.check_createBug())

    @classmethod
    def tearDownClass(cls):
        cls.page.quit()