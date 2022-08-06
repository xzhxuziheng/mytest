from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

if __name__ == '__main__':
    # 设置终端参数
    desired_caps = {
        'platformName': 'Android',
        'platformVersion': '7.1.2',
        'deviceName': 'Huawei Mate 30 5G',
        'appPackage': 'com.ledear.rental',
        'appActivity': 'com.ledear.rental.activity.SplashActivity',
        'noReset': True
    }

    driver = webdriver.Remote('127.0.0.1:4723/wd/hub', desired_caps)
    el_phone = driver.find_element(AppiumBy.ID, 'com.ledear.rental:id/et_phone').send_keys('19180930619')
    el_password = driver.find_element(AppiumBy.ID, 'com.ledear.rental:id/et_pwd').send_keys('111111')
    driver.find_element(AppiumBy.ID, 'com.ledear.rental:id/tv_login').click()
    driver.implicitly_wait(3)
    # 点击商户中心
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("商户中心")').click()
    driver.implicitly_wait(3)
    # 点击退出登录
    driver.find_element(AppiumBy.ID, 'com.ledear.rental:id/tv_logout').click()
    driver.implicitly_wait(3)
    # 点击确认
    driver.find_element(AppiumBy.ID, 'com.ledear.rental:id/tv_call').click()
