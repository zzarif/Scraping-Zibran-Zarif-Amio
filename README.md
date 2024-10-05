
# Scraping Engineer Project - Zibran Zarif Amio

Zelf Hackathon 2.0

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

All the scripts are available at [scraper](/scraper/) directory.

# Bonus



# Contact

