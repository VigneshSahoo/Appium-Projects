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
            button1 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
            self.assertTrue(button1.is_displayed())
            button1.click()
            button2 = self.driver.find_element_by_id("com.augray.avmessage:id/gettingStarted")
            self.assertTrue(button2.is_displayed())
            button2.click()
            button3 = self.driver.find_element_by_id("com.augray.avmessage:id/googleSignup")
            self.assertTrue(button3.is_displayed())
            button3.click()
            button4 = self.driver.find_element_by_id("com.google.android.gms:id/account_display_name")
            self.assertTrue(button4.is_displayed())
            button4.click()
            print('Login Successful!')
        except NoSuchElementException:
            print('Login Failed! Element not found')

    def test_2_create_avatar(self):
        print('Creating Avatar. Please wait...')
        try:
            button5 = self.driver.find_element_by_id("android:id/button2")
            self.assertTrue(button5.is_displayed())
            button5.click()
            button6 = self.driver.find_element_by_id("com.augray.avmessage:id/chat_bot_footer")
            self.assertTrue(button6.is_displayed())
            button6.click()
            time.sleep(15)
            button7 = self.driver.find_element_by_id("com.augray.avmessage:id/layout_add_avatar")
            self.assertTrue(button7.is_displayed())
            button7.click()
            time.sleep(2)
            button8 = self.driver.find_element_by_id("com.augray.avmessage:id/imgBtnAddNewAvatar")
            self.assertTrue(button8.is_displayed())
            button8.click()
            button9 = self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
            self.assertTrue(button9.is_displayed())
            button9.click()
            time.sleep(5)
            button10 = self.driver.find_element_by_id("com.augray.avmessage:id/imgBtnGallery")
            self.assertTrue(button10.is_displayed())
            button10.click()
            button11 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[7]/android.widget.LinearLayout/android.widget.TextView")
            self.assertTrue(button11.is_displayed())
            button11.click()
            button12 = driver.find_element_by_id("com.sec.android.gallery3d:id/thumbnail")
            self.assertTrue(button12.is_displayed())
            button12.click()
            button13 = driver.find_element_by_xpath("(//android.widget.FrameLayout[@content-desc=\"Button\"])[1]/android.widget.ImageView")
            self.assertTrue(button13.is_displayed())
            button13.click()
            button14 = driver.find_element_by_id("com.augray.avmessage:id/crop_image_menu_crop")
            self.assertTrue(button14.is_displayed())
            button14.click()
            button15 = self.driver.find_element_by_id("com.augray.avmessage:id/imgBtnMale")
            self.assertTrue(button15.is_displayed())
            button15.click()
            time.sleep(20)
            button16 = self.driver.find_element_by_id("com.augray.avmessage:id/imgBtnSaveAvatar")
            self.assertTrue(button16.is_displayed())
            button16.click()
            time.sleep(20)
            button17 = self.driver.find_element_by_id("com.augray.avmessage:id/backHomeLayout")
            self.assertTrue(button17.is_displayed())
            button17.click()
            time.sleep(5)
            button18 = self.driver.find_element_by_id("com.augray.avmessage:id/backHomeLayout")
            self.assertTrue(button18.is_displayed())
            button18.click()
            print('Avatar created successfully!')
        except NoSuchElementException:
            print('Avatar Creation Failed!')
            print(traceback.format_exc(limit=1))

if __name__ == '__main__':
    unittest.main()
