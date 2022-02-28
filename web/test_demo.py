from pprint import pprint
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo:
    def setup_method(self, method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_demo(self):
        self.driver.get("https://ceshiren.com/")
        pprint(self.driver.get_cookies())
        cookies = [{'domain': 'ceshiren.com',
                    'httpOnly': True,
                    'name': '_forum_session',
                    'path': '/',
                    'sameSite': 'Lax',
                    'secure': True,
                    'value': 'dFdmUW9Qb0lzbDR6NUEzQXBrcFhYMGY4b3o5TnJ1KzRDeElSdVNpdkpxdnlQSkxETWh0QUhhbnQ1Z0UzU2d2YWRZTWMwV3JrdU9hT241MHIwaUhJY215anJXUDJyYStFWlBCdWFzcElzakJSYnBVT1VXYlJwcEhGZnk4TFpiNmhBWUZlTm00S2FPVUc5eGtCUXpDTHltbGU4QXZtakJ0dWxBR3BwNURhQWlqSnFocllTNlJCU1kvcEVrV2JIb1pLLS1CcmVSWUN6b3VEbk9IUWdjdUo2RWVRPT0%3D--413541f511cc673f3bab00156b330ca6696ee4a0'},
                   {'domain': '.ceshiren.com',
                    'expiry': 1677585615,
                    'httpOnly': False,
                    'name': 'Hm_lvt_214f62eef822bde113f63fedcab70931',
                    'path': '/',
                    'secure': False,
                    'value': '1646048596,1646048660,1646048740,1646049616'},
                   {'domain': 'ceshiren.com',
                    'expiry': 1651233615,
                    'httpOnly': True,
                    'name': '_t',
                    'path': '/',
                    'sameSite': 'Lax',
                    'secure': True,
                    'value': 'bFM4Q1VCc3NyOXNYQ0pNdHFlalFuc3hzdjExUlVoL0lud3dWVHhFZlNmUlRaWEI1NWZZL3M2aGpGVXF6L0ZNaVd2WnRNQmxXQzhvbkU3TCtzbSt2Vm5zYmhxN20vWmprNFgwSklxK1N5UTExWEt0OGVCczVnZDhzZDA4ZE9zSk1ubEN2SlNqM0hORXhCdXFpZzNWOURLb2xHcDY2REdJYXBmejlXdHBzcG9PbmJzL3ppRWpDVi83MlFxN3FOUUVoOW80OS9aaXE2akxBazQvWndPOGlxWGtocWxMNC9yMmRaaUk0ME1SR1lxQnR6bE5MZVV2cm5JOGR4V3FKajVUQWNERm8xQ00wK0NDWUZLQTNlNUg5SXc9PS0tcDYwK3k3SnhveVVmTUlDaUc3akpSQT09--5f74cc462341bc27ed514a77266549406ad460b5'},
                   {'domain': '.ceshiren.com',
                    'httpOnly': False,
                    'name': 'Hm_lpvt_214f62eef822bde113f63fedcab70931',
                    'path': '/',
                    'secure': False,
                    'value': '1646049616'},
                   {'domain': '.ceshiren.com',
                    'expiry': 1646136015,
                    'httpOnly': False,
                    'name': '_gid',
                    'path': '/',
                    'secure': False,
                    'value': 'GA1.2.119398057.1646039830'},
                   {'domain': '.ceshiren.com',
                    'expiry': 1709121615,
                    'httpOnly': False,
                    'name': '_ga',
                    'path': '/',
                    'secure': False,
                    'value': 'GA1.2.1094891058.1645948906'}]
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://ceshiren.com/")
        pprint(self.driver.get_cookies())
        sleep(3)
        # self.driver.find_element(By.LINK_TEXT, "所有分类").click()
