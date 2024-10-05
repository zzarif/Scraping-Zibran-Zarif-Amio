from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import urllib.parse
import pandas as pd
import time
import os

def scrape_tiktok_keywords(keywords):
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--start-maximized")
    options.add_argument("--window_size=1920,1080")
    options.add_argument(r"--user-data-dir=C:\Users\zzami\AppData\Local\Google\Chrome\User Data")
    options.add_argument(r'--profile-directory=Default')
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(options=options)

    all_posts = []

    for keyword in keywords:
        search_url = f"https://www.tiktok.com/search/video?q={urllib.parse.quote(keyword)}"
        driver.get(search_url)
        
        # Wait for the video posts to load
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#tabs-0-panel-search_video > div > div"))
            )
        except TimeoutException:
            print(f"Timeout waiting for videos to load for keyword: {keyword}")
            continue
        
        # Scroll to load more videos (need to adjust this)
        for _ in range(2):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        
        video_posts = driver.find_elements(By.CSS_SELECTOR, "#tabs-0-panel-search_video > div > div > div")
        print(len(video_posts))

        for post in video_posts:
            try:
                video_url = post.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                video_caption = post.find_element(By.CSS_SELECTOR, "div[data-e2e='search-card-video-caption']").text
                author_username = post.find_element(By.CSS_SELECTOR, "a[data-e2e='search-card-user-link']").text
                author_url = post.find_element(By.CSS_SELECTOR, "a[data-e2e='search-card-user-link']").get_attribute("href")
                
                all_posts.append({
                    "keyword": keyword,
                    "video_url": video_url,
                    "video_caption": video_caption,
                    "author_username": author_username,
                    "author_url": author_url
                })

                df = pd.DataFrame(data=all_posts, columns=all_posts[0].keys())
                data_dir = os.path.join(os.getcwd(), 'data', 'keyword_posts.csv')
                df.to_csv(data_dir, index=False)

            except Exception as e:
                print(f"Error scraping post: {e}")
    
    driver.quit()

# Example usage
keywords = [
    "beautiful destinations",
    "places to visit",
    # "places to travel",
    # "places that don't feel real",
    # "travel hacks"
]

scrape_tiktok_keywords(keywords)