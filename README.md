
<h1 align="center">
  <br>
  Zelf Hackathon 2.0 - Scraping Engineer - Zibran Zarif Amio
  <br>
</h1>


A scraping system that collects data from TikTok, based on specified keywords and hashtags, and then analyzes that data to identify top influencers in the tourism industry. The project includes key features such as keyword & hashtag scraping, profile information scraping, and influencer identification.

# Scraped Data

There are 3 files in the [data](/data/) directory. The files are:

1. [`keyword_posts.csv`](/data/keyword_posts.csv): Has all the video post data for the given search keywords.
2. [`hashtag_posts.csv`](/data/hashtag_posts.csv): Has all the video post data for the given hashtags.
3. [`top_influencers.csv`](/data/top_influencers.csv): Has all the influencer's data that have at least 100k followers an have received over 1 million likes.

# Build from Source

1. Clone the repo

```bash
git clone https://github.com/zzarif/Scraping-Zibran-Zarif-Amio
cd Scraping-Zibran-Zarif-Amio/
```

2. Initialize and activate virtual environment

```bash
virtualenv venv
source venv/Scripts/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

_Note: Select virtual environment interpreter from_ `Ctrl`+`Shift`+`P`

4. Run **Keyword** scraper with specified scroll count (I used `2` due to time constraints, you can use as much as you want):
```bash
python scraper/keyword_scraper.py --scroll 2
```

5. Run **Hashtag** scraper with specified scroll count (I used `2` due to time constraints, you can use as much as you want):
```bash
python scraper/hashtag_scraper.py --scroll 2
```

6. Run Author info scraper with specified scroll count:
```bash
python scraper/author_info_scraper.py
```

7. Run analysis of top influencers:
```bash
python analysis/top_influencers.py
```

All the scripts are available at [scraper](/scraper/) and [analysis](/analysis/) directory.

# Bonus

1. Like a TikTok video given its URL:
```bash
python bonus/like_video.py --video_url https://www.tiktok.com/@epicexploring/video/7415640201051000097
```

2. Comment on a TikTok video given its URL and comment content:
```bash
python bonus/comment_on_video.py --video_url https://www.tiktok.com/@epicexploring/video/7415640201051000097 --comment "nice"
```

3. Verify whether your comment exists:
```bash
python bonus/comment_verifier.py --video_url https://www.tiktok.com/@epicexploring/video/7415640201051000097 --my_name "zibranzarif"
```

# Contact

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/zibran-zarif-amio-b82717263/) [![Mail](https://img.shields.io/badge/Gmail-EA4335?logo=gmail&logoColor=fff)](mailto:zibran.zarif.amio@gmail.com)

Thank you so much for your interest. Would love your valuable feedback!