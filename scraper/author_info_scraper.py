import pandas as pd
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


def convert_to_numeric(value):
    if isinstance(value, str):
        value = value.lower().replace(',', '')  # Remove commas
        if 'k' in value:
            return int(float(value.replace('k', '')) * 1000)
        elif 'm' in value:
            return int(float(value.replace('m', '')) * 1000000)
        elif 'b' in value:
            return int(float(value.replace('b', '')) * 1000000000)
        else:
            return int(float(value))
    return value

def scrape_author_data(driver, author_url):
    driver.get(author_url)
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h2[data-e2e='user-subtitle']"))
        )
    except TimeoutException:
        print(f"Timeout waiting for author page to load: {author_url}")
        return None, None, None

    try:
        following_count = driver.find_element(By.CSS_SELECTOR, "[data-e2e='following-count']").text
        followers_count = driver.find_element(By.CSS_SELECTOR, "[data-e2e='followers-count']").text
        likes_count = driver.find_element(By.CSS_SELECTOR, "[data-e2e='likes-count']").text

        return (convert_to_numeric(following_count),
                convert_to_numeric(followers_count),
                convert_to_numeric(likes_count))
    except NoSuchElementException:
        print(f"Could not find stats for author: {author_url}")
        return None, None, None

def process_csv(file_path, driver):
    df = pd.read_csv(file_path)
    
    # Initialize new columns with None
    df['following_count'] = None
    df['followers_count'] = None
    df['likes_count'] = None

    for index, row in df.iterrows():
        author_url = row['author_url']
        following_count, followers_count, likes_count = scrape_author_data(driver, author_url)
        
        # Update the DataFrame row by row
        df.at[index, 'following_count'] = following_count
        df.at[index, 'followers_count'] = followers_count
        df.at[index, 'likes_count'] = likes_count
        
        print(f"Processed {index + 1}/{len(df)} rows")
        time.sleep(2)  # Add a delay to avoid overwhelming the server

    df.to_csv(file_path, index=False)
    print(f"Updated {file_path} with new data.")


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument("--start-maximized")
    options.add_argument("--window_size=1920,1080")
    options.add_argument(r"--user-data-dir=C:\Users\zzami\AppData\Local\Google\Chrome\User Data")
    options.add_argument(r'--profile-directory=Default')
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(options=options)

    try:
        process_csv(os.path.join(os.getcwd(), 'data', 'keyword_posts.csv'), driver)
        process_csv(os.path.join(os.getcwd(), 'data', 'hashtag_posts.csv'), driver)
    finally:
        driver.quit()