from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

if __name__ == '__main__':
    # desired_caps = {
    #     'platformName': 'Android',
    #     'platformVersion': '7.1.2',
    #     'deviceName': 'Huawei Mate 30 5G',
    #     'appPackage': 'com.tencent.mm',
    #     'appActivity': 'com.tencent.mm.ui.LauncherUI',
    #     'noReset': True
    # }
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '12.0.0',
        'deviceName': 'OPPO Find X3',
        'appPackage': 'com.tencent.mm',
        'appActivity': 'com.tencent.mm.ui.LauncherUI',
        'noReset': True
    }
    driver = webdriver.Remote('127.0.0.1:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("发现")').click()
    # driver.implicitly_wait(10)
    # driver.find_element(AppiumBy.ID, 'com.tencent.mm:id/he6').click()
    driver.implicitly_wait(10)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("小程序")').click()
    driver.implicitly_wait(10)
    driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]').click()
    # driver.implicitly_wait(60)
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("微信一键登录")').click()
    # driver.implicitly_wait(10)
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("允许")').click()
    # driver.implicitly_wait(10)
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("08月03日")').click()
    # driver.implicitly_wait(10)
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("3")').click()
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("4")').click()
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("确认")').click()
    # driver.implicitly_wait(10)
    # driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.tencent.mm:id/biv"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView[1]/android.view.View[3]/android.view.View[6]').click()
    # driver.implicitly_wait(10)
    # driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.tencent.mm:id/biv"]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.RelativeLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView[1]/android.view.View[6]/android.view.View[1]/android.view.View[8]').click()
    # driver.implicitly_wait(10)
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("去选车")').click()
    # driver.implicitly_wait(10)
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("历史车型3")').click()
    # driver.implicitly_wait(10)
    # driver.find_element(AppiumBy.XPATH, '//android.widget.RadioButton/android.view.View[1]').click()
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("￥0.07  确认订单")').click()
    # driver.implicitly_wait(60)
    # # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("忽略")').click()
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")').click()
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("4")').click()
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("7")').click()
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("2")').click()
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("5")').click()
    # driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("8")').click()
    # driver.implicitly_wait(10)
    driver.implicitly_wait(60)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("去支付")').click()
    driver.implicitly_wait(10)
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("1")').click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("4")').click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("7")').click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("2")').click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("5")').click()
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("8")').click()
