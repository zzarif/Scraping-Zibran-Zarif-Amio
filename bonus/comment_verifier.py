from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import urllib.parse
import pandas as pd
import argparse
import time
import os


parser = argparse.ArgumentParser()
parser.add_argument('--video_url', type=str, default="https://www.tiktok.com/@epicexploring/video/7415640201051000097", help='Specify TikTok video URL')
parser.add_argument('--my_name', type=str, default="Zibran Zarif", help='Specify your name')
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
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'DivCommentContainer')]"))
        )

        # Find all buttons within the container
        comments = driver.find_element(By.XPATH, "//div[contains(@class, 'DivCommentContainer')]").text

        if args.my_name in comments:
            print("My comment exists")
        else:
            print("It does not exist.")
        

    except TimeoutException:
        print(f"Timeout waiting for video to load")
    
    driver.quit()