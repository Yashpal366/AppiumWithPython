from appium import webdriver
from selenium.webdriver.common.by import By
import time

class TestYouTubeSearch:
    def setup_method(self):
        # Desired capabilities for the Android device
        desired_caps = {
            'platformName': 'Android',
            'deviceName': 'Android Emulator',  
            'appPackage': 'com.google.android.youtube', 
            'appActivity': 'com.google.android.youtube.HomeActivity',  
            'automationName': 'UiAutomator2'
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def teardown_method(self):
        # Close the driver after the test
        self.driver.quit()

    def test_youtube_search(self):
        # Wait for the YouTube app to load
        time.sleep(5)

        # Click on the search icon
        search_icon = self.driver.find_element(By.ID, 'com.google.android.youtube:id/menu_item_1')
        search_icon.click()

        # Wait for the search bar to appear
        time.sleep(2)

        # Enter a search query in the search bar
        search_bar = self.driver.find_element(By.ID, 'com.google.android.youtube:id/search_edit_text')
        search_bar.send_keys('Python tutorials')

        # Press the search button on the keyboard
        self.driver.press_keycode(66)  # 66 is the Android keycode for "Enter"

        # Wait for search results to load
        time.sleep(5)

        # Check if the search results contain the word "Python"
        search_results = self.driver.find_elements(By.ID, 'com.google.android.youtube:id/title')

        assert any('Python' in result.text for result in search_results), "Search results did not contain 'Python'"

if __name__ == "__main__":
    test = TestYouTubeSearch()
    test.setup_method()
    test.test_youtube_search()
    test.teardown_method()
