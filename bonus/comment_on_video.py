from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import argparse
import time


parser = argparse.ArgumentParser()
parser.add_argument('--video_url', type=str, default="https://www.tiktok.com/@epicexploring/video/7415640201051000097", help='Specify TikTok video URL')
parser.add_argument('--comment', type=str, default="nice", help='Specify comment')
args = parser.parse_args()


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--start-maximized")
    options.add_argument("--window_size=1920,1080")
    options.add_argument(r"--user-data-dir=C:\Users\zzami\AppData\Local\Google\Chrome\User Data")
    options.add_argument(r'--profile-directory=Default')
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(options=options)
    
    driver.get(args.video_url)
    
    # Wait for the video button to load
    try:
        # Find the div with "DivActionItemContainer" in its class name
        action_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@contenteditable='true']"))
        )

        # Find all buttons within the container
        input = driver.find_element(By.XPATH, "//div[@contenteditable='true']")
        input.click()
        input.clear()
        input.send_keys(args.comment)

        # Wait for a moment
        time.sleep(2)

        post_btn = driver.find_element(By.XPATH, "//div[@data-e2e='comment-post']")
        post_btn.click()

        time.sleep(1)
        
        input.clear()
        time.sleep(5)



    except TimeoutException:
        print(f"Timeout waiting for video to load")
    
    driver.quit()