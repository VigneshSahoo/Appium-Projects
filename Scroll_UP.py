"""
Test Details:
Device used: Samsung S10
Device ID: RZ8M30525CH
Tools Used: Appium, Android Studio and ADB
IDE: PyCharm

Basic Requirements:
1. At-least one google account should be added in the Android device.
2. User have already created an account in TaDa Time App.

**Please note that this test is not applicable for a new user.
"""

import time
import traceback
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException


class TaDaTime(unittest.TestCase):

    def setUp(self):
        desired_inputs = {
            "deviceName": "RZ8M30525CH",  # Android Device ID
            "platformName": "android",
            "appPackage": "com.augray.avmessage",
            "appActivity": ".Signup.SplashActivity",
            "noReset": True
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_inputs)
        self.driver.implicitly_wait(15)

    def test_1_scroll_up(self):
        print('Running Login Check. Please wait...')
        try:
            button5 = self.driver.find_element_by_id("android:id/button2")
            self.assertTrue(button5.is_displayed())
            button5.click()
            button6 = driver.find_element_by_accessibility_id("Latest")
            self.assertTrue(button6.is_displayed())
            button6.click()
            time.sleep(10)
            count = 1
            while count < 51:
                driver.get_screenshot_as_file('file' + str(count) + '.png')
                TouchAction(driver).long_press(element1, x=550, y=2000, duration=45000).move_to(x=500, y=10).release().perform()
                count = count + 1
        except:
            pass
