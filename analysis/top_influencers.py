import pandas as pd
import os


def analyze_influencers(input_files, output_file):
    # Read and concatenate all input files
    dfs = [pd.read_csv(file) for file in input_files]
    combined_df = pd.concat(dfs, ignore_index=True)

    # Filter for top influencers
    top_influencers = combined_df[
        (combined_df['followers_count'] >= 100000) & 
        (combined_df['likes_count'] >= 1000000)
    ]

    # Select relevant columns and remove duplicates
    top_influencers = top_influencers[['author_username', 'author_url', 'followers_count', 'likes_count']]
    top_influencers = top_influencers.drop_duplicates(subset=['author_username', 'author_url'])

    # Sort by followers_count in descending order
    top_influencers = top_influencers.sort_values('followers_count', ascending=False)

    # Save to CSV
    top_influencers.to_csv(output_file, index=False)
    print(f"Top influencers saved to {output_file}")
    print(f"Total number of top influencers: {len(top_influencers)}")


if __name__ == "__main__":
    input_files = [os.path.join(os.getcwd(), 'data', 'keyword_posts.csv'), os.path.join(os.getcwd(), 'data', 'hashtag_posts.csv')]
    output_file = os.path.join(os.getcwd(), 'data', 'top_influencers.csv')
    analyze_influencers(input_files, output_file)