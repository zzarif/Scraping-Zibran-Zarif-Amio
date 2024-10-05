from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd
import argparse
import time
import os


parser = argparse.ArgumentParser()
parser.add_argument('--scroll', type=int, default=2, help='Specify scroll count')
args = parser.parse_args()


def scrape_tiktok_hashtags(hashtags):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--start-maximized")
    options.add_argument("--window_size=1920,1080")
    options.add_argument(r"--user-data-dir=C:\Users\zzami\AppData\Local\Google\Chrome\User Data")
    options.add_argument(r'--profile-directory=Default')
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(options=options)
    
    all_posts = []

    for hashtag in hashtags:
        hashtag_url = f"https://www.tiktok.com/tag/{hashtag}"
        driver.get(hashtag_url)
        
        # Wait for the video posts to load
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-e2e='challenge-item-list'] > div"))
            )
        except TimeoutException:
            print(f"Timeout waiting for videos to load for hashtag: {hashtag}")
            continue
        
        # Scroll to load more videos (need to adjust this)
        for _ in range(args.scroll):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        
        video_posts = driver.find_elements(By.CSS_SELECTOR, "div[data-e2e='challenge-item-list'] > div")
        
        for post in video_posts:
            try:
                video_url = post.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                video_caption = post.find_element(By.CSS_SELECTOR, "div[data-e2e='challenge-item-desc']").text
                author_username = post.find_element(By.CSS_SELECTOR, "p[data-e2e='challenge-item-username']").text
                author_url = post.find_element(By.CSS_SELECTOR, "a[data-e2e='challenge-item-avatar']").get_attribute("href").split('?')[0]
                
                all_posts.append({
                    "hashtag": hashtag,
                    "video_url": video_url,
                    "video_caption": video_caption,
                    "author_username": author_username,
                    "author_url": author_url
                })

                df = pd.DataFrame(data=all_posts, columns=all_posts[0].keys())
                data_dir = os.path.join(os.getcwd(), 'data', 'hashtag_posts.csv')
                df.to_csv(data_dir, index=False)

            except Exception as e:
                print(f"Error scraping post: {e}")
    
    driver.quit()

# Example usage
hashtags = [
    "traveltok",
    "wanderlust",
    # "backpackingadventures",
    # "luxurytravel",
    # "hiddengems",
    # "solotravel", 
    # "roadtripvibes", 
    # "travelhacks", 
    # "foodietravel", 
    # "sustainabletravel"
]

scrape_tiktok_hashtags(hashtags)