import pytest
from selenium.webdriver.common.by import By
import time


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass


class TestHubSpot(BaseTest):

    @pytest.mark.parametrize(
        "username , password",
        [
            ("kdpatel8184@gmail.com", "admin123"),
            ("dpatel2030@gmail.com", "pwd1234"),
        ]
    )
    def test_login(self, username, password):
        """
        This method is use to login to hubspot application
        : param username:
        : param password:
        : return:
        """

        self.driver.get("https://classic.crmpro.com/")
        self.driver.find_element(By.NAME, 'username').send_keys(username)
        self.driver.find_element(By.NAME, 'password').send_keys(password)

