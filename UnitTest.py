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

    def test_1_login_check(self):
        print('Running Login Check. Please wait...')
        try:
            self.driver.get_screenshot_as_file('button1.png')
            button1 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
            self.assertTrue(button1.is_displayed())
            button1.click()
            self.driver.get_screenshot_as_file('button2.png')
            button2 = self.driver.find_element_by_id("com.augray.avmessage:id/gettingStarted")
            self.assertTrue(button2.is_displayed())
            button2.click()
            self.driver.get_screenshot_as_file('button3.png')
            button3 = self.driver.find_element_by_id("com.augray.avmessage:id/googleSignup")
            self.assertTrue(button3.is_displayed())
            button3.click()
            self.driver.get_screenshot_as_file('button4.png')
            button4 = self.driver.find_element_by_id("com.google.android.gms:id/account_display_name")
            self.assertTrue(button4.is_displayed())
            button4.click()
            print('Login Successful!')
        except NoSuchElementException:
            self.driver.get_screenshot_as_file('error_login.png')
            print('Login Failed! Element not found')

    def test_2_create_avatar(self):
        print('Creating Avatar. Please wait...')
        try:
            self.driver.get_screenshot_as_file('button5.png')
            button5 = self.driver.find_element_by_id("android:id/button2")
            self.assertTrue(button5.is_displayed())
            button5.click()
            self.driver.get_screenshot_as_file('button6.png')
            button6 = self.driver.find_element_by_id("com.augray.avmessage:id/chat_bot_footer")
            self.assertTrue(button6.is_displayed())
            button6.click()
            time.sleep(15)
            self.driver.get_screenshot_as_file('button7.png')
            button7 = self.driver.find_element_by_id("com.augray.avmessage:id/layout_add_avatar")
            self.assertTrue(button7.is_displayed())
            button7.click()
            time.sleep(2)
            self.driver.get_screenshot_as_file('button8.png')
            button8 = self.driver.find_element_by_id("com.augray.avmessage:id/imgBtnAddNewAvatar")
            self.assertTrue(button8.is_displayed())
            button8.click()
            self.driver.get_screenshot_as_file('button9.png')
            button9 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
            self.assertTrue(button9.is_displayed())
            button9.click()
            time.sleep(5)
            self.driver.get_screenshot_as_file('button10.png')
            button10 = self.driver.find_element_by_id("com.augray.avmessage:id/imgBtnTakePicture")
            self.assertTrue(button10.is_displayed())
            button10.click()
            self.driver.get_screenshot_as_file('button11.png')
            button11 = self.driver.find_element_by_id("com.augray.avmessage:id/imgBtnMale")
            self.assertTrue(button11.is_displayed())
            button11.click()
            time.sleep(20)
            self.driver.get_screenshot_as_file('button12.png')
            button12 = self.driver.find_element_by_id("com.augray.avmessage:id/imgBtnSaveAvatar")
            self.assertTrue(button12.is_displayed())
            button12.click()
            time.sleep(20)
            self.driver.get_screenshot_as_file('button13.png')
            button13 = self.driver.find_element_by_id("com.augray.avmessage:id/backHomeLayout")
            self.assertTrue(button13.is_displayed())
            button13.click()
            time.sleep(5)
            self.driver.get_screenshot_as_file('button14.png')
            button14 = self.driver.find_element_by_id("com.augray.avmessage:id/backHomeLayout")
            self.assertTrue(button14.is_displayed())
            button14.click()
            print('Avatar created successfully!')
        except NoSuchElementException:
            print('Avatar Creation Failed!')
            print(traceback.format_exc(limit=1))
            self.driver.get_screenshot_as_file('error_create_avatar.png')

    def test_3_compose_avatar(self):
        print('Composing the Avatar. Please wait...')
        try:
            button5 = self.driver.find_element_by_id("android:id/button2")
            self.assertTrue(button5.is_displayed())
            button5.click()
            self.driver.get_screenshot_as_file('button15.png')
            button15 = self.driver.find_element_by_id("com.augray.avmessage:id/fab_avatar_compose")
            self.assertTrue(button15.is_displayed())
            button15.click()
            time.sleep(10)
            TouchAction(self.driver).tap(x=336, y=1886).perform()
            time.sleep(10)
            button16 = self.driver.find_element_by_id("com.augray.avmessage:id/imgBtnSaveAvatar")
            self.assertTrue(button16.is_displayed())
            button16.click()
            self.driver.get_screenshot_as_file('button16.png')
            print('Avatar composition has been saved successfully!')
        except NoSuchElementException:
            print('Avatar Composing Failed!')
            print(traceback.format_exc(limit=1))
            self.driver.get_screenshot_as_file('error_compose_avatar.png')

    def test_4_recording_feed(self):
        self.test_3_compose_avatar()
        print('Recording Feed. Please wait...')
        try:
            self.driver.get_screenshot_as_file('button17.png')
            button17 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
            self.assertTrue(button17.is_displayed())
            button17.click()
            self.driver.get_screenshot_as_file('button18.png')
            button18 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
            self.assertTrue(button18.is_displayed())
            button18.click()
            time.sleep(20)  # Scan the surface slowly
            TouchAction(self.driver).tap(x=552, y=995).perform()
            time.sleep(2)
            TouchAction(self.driver).tap(x=552, y=995).perform()
            time.sleep(2)
            self.driver.get_screenshot_as_file('button19.png')
            button19 = self.driver.find_element_by_id("com.augray.avmessage:id/imgBtnARAvtarVideo")
            self.assertTrue(button19.is_displayed())
            button19.click()
            time.sleep(3)
            self.driver.get_screenshot_as_file('button20.png')
            button20 = self.driver.find_element_by_id("com.augray.avmessage:id/imgBtnARStopRecording")
            self.assertTrue(button20.is_displayed())
            button20.click()
            time.sleep(3)
            print('Feed has been recorded successfully!')
        except NoSuchElementException:
            print('Recording Feed Failed!')
            print(traceback.format_exc(limit=1))
            self.driver.get_screenshot_as_file('error_recording_feed.png')

    def test_5_post_feed(self):
        self.test_3_compose_avatar()
        self.test_4_recording_feed()
        print('Posting Feed. Please wait...')
        try:
            self.driver.get_screenshot_as_file('button21.png')
            button21 = self.driver.find_element_by_id("com.augray.avmessage:id/etxtPostTitle")
            self.assertTrue(button21.is_displayed())
            button21.click()
            time.sleep(3)
            TouchAction(self.driver).tap(x=225, y=1746).perform()  # S
            TouchAction(self.driver).tap(x=117, y=1746).perform()  # A
            TouchAction(self.driver).tap(x=852, y=1891).perform()  # M
            TouchAction(self.driver).tap(x=1007, y=1600).perform()  # P
            TouchAction(self.driver).tap(x=954, y=1734).perform()  # L
            TouchAction(self.driver).tap(x=277, y=1585).perform()  # E
            TouchAction(self.driver).tap(x=64, y=1462).perform()  # 1
            self.driver.get_screenshot_as_file('button22.png')
            button22 = self.driver.find_element_by_id("com.augray.avmessage:id/imgBtnAvtarVideoSendFeed")
            self.assertTrue(button22.is_displayed())
            button22.click()
            time.sleep(3)
            self.driver.get_screenshot_as_file('button23.png')
            button23 = self.driver.find_element_by_id("com.augray.avmessage:id/txtBtnSend")
            self.assertTrue(button23.is_displayed())
            button23.click()
            time.sleep(3)
            self.driver.get_screenshot_as_file('button24.png')
            button24 = self.driver.find_element_by_id("com.augray.avmessage:id/txtBtnVideoShare")
            self.assertTrue(button24.is_displayed())
            button24.click()
            print('Feed has been uploaded successfully!')
            self.driver.get_screenshot_as_file('button25.png')
        except NoSuchElementException:
            print('Uploading Feed Failed!')
            print(traceback.format_exc(limit=1))
            self.driver.get_screenshot_as_file('error_posting_feed.png')


if __name__ == '__main__':
    unittest.main()
