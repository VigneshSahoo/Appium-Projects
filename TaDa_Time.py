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
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_inputs = {
    "deviceName": "RZ8M30525CH",  # Android Device ID
    "platformName": "android",
    "appPackage": "com.augray.avmessage",
    "appActivity": ".Signup.SplashActivity",
    "noReset": False  # If you would like to continue the test from some specific button, comment out the rest and
                      # set this parameter to True
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_inputs)
driver.implicitly_wait(15)
button1 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
button1.click()
button2 = driver.find_element_by_id("com.augray.avmessage:id/gettingStarted")
button2.click()
button3 = driver.find_element_by_id("com.augray.avmessage:id/googleSignup")
button3.click()
button4 = driver.find_element_by_id("com.google.android.gms:id/account_display_name")
button4.click()
button5 = driver.find_element_by_id("android:id/button2")
button5.click()
button6 = driver.find_element_by_id("com.augray.avmessage:id/chat_bot_footer")
button6.click()
time.sleep(15)
button7 = driver.find_element_by_id("com.augray.avmessage:id/layout_add_avatar")
button7.click()
time.sleep(2)
button8 = driver.find_element_by_id("com.augray.avmessage:id/imgBtnAddNewAvatar")
button8.click()
button9 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
button9.click()
time.sleep(5)
button10 = driver.find_element_by_id("com.augray.avmessage:id/imgBtnTakePicture")
button10.click()
button11 = driver.find_element_by_id("com.augray.avmessage:id/imgBtnMale")
button11.click()
time.sleep(20)
button12 = driver.find_element_by_id("com.augray.avmessage:id/imgBtnSaveAvatar")
button12.click()
time.sleep(20)
button13 = driver.find_element_by_id("com.augray.avmessage:id/backHomeLayout")
button13.click()
time.sleep(5)
button14 = driver.find_element_by_id("com.augray.avmessage:id/backHomeLayout")
button14.click()
button15 = driver.find_element_by_id("com.augray.avmessage:id/fab_avatar_compose")
button15.click()
time.sleep(10)
TouchAction(driver).tap(x=336, y=1886).perform()  # Change the coordinates according to the Mobile's Resolution
time.sleep(10)
button16 = driver.find_element_by_id("com.augray.avmessage:id/imgBtnSaveAvatar")
button16.click()
button17 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
button17.click()
button18 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
button18.click()
# el18 = driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")
# el18.click()
time.sleep(20)  # Scan the surface slowly
TouchAction(driver).tap(x=552, y=995).perform()
time.sleep(2)
TouchAction(driver).tap(x=552, y=995).perform()
time.sleep(2)
button19 = driver.find_element_by_id("com.augray.avmessage:id/imgBtnARAvtarVideo")
button19.click()
time.sleep(3)
button20 = driver.find_element_by_id("com.augray.avmessage:id/imgBtnARStopRecording")
button20.click()
time.sleep(3)
button21 = driver.find_element_by_id("com.augray.avmessage:id/etxtPostTitle")
button21.click()
time.sleep(3)
# Naming the video as 'Sample1'
TouchAction(driver).tap(x=225, y=1746).perform()
TouchAction(driver).tap(x=117, y=1746).perform()
TouchAction(driver).tap(x=852, y=1891).perform()
TouchAction(driver).tap(x=1007, y=1600).perform()
TouchAction(driver).tap(x=954, y=1734).perform()
TouchAction(driver).tap(x=277, y=1585).perform()
TouchAction(driver).tap(x=64, y=1462).perform()
button22 = driver.find_element_by_id("com.augray.avmessage:id/imgBtnAvtarVideoSendFeed")
button22.click()
time.sleep(3)
button23 = driver.find_element_by_id("com.augray.avmessage:id/txtBtnSend")
button23.click()
time.sleep(3)
button24 = driver.find_element_by_id("com.augray.avmessage:id/txtBtnVideoShare")
button24.click()
print("You have successfully uploaded a feed!")
