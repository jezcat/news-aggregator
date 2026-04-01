#!/usr/bin/env python3
"""
News Aggregator Script

This script aggregates news headlines from multiple RSS feeds.
It uses the feedparser library to parse RSS feeds and display the latest news.
"""

import feedparser

# List of RSS feed URLs from popular news sites
RSS_FEEDS = [
    'http://feeds.bbci.co.uk/news/rss.xml',  # BBC News
    'http://rss.cnn.com/rss/edition.rss',    # CNN
    'https://feeds.npr.org/1001/rss.xml',   # NPR
    # Add more feeds as needed
]

def aggregate_news():
    """
    Fetches and aggregates news from the RSS feeds.
    Prints the title, link, and summary for each entry.
    """
    all_entries = []

    for feed_url in RSS_FEEDS:
        print(f"Fetching news from: {feed_url}")
        feed = feedparser.parse(feed_url)

        if feed.bozo:  # Check for parsing errors
            print(f"Error parsing feed: {feed_url}")
            continue

        for entry in feed.entries[:5]:  # Limit to 5 entries per feed
            all_entries.append({
                'title': entry.title,
                'link': entry.link,
                'summary': entry.summary if 'summary' in entry else 'No summary available',
                'published': entry.published if 'published' in entry else 'Unknown'
            })

    # Sort entries by published date (if available), newest first
    # For simplicity, we'll just print them as is
    print("\nAggregated News Headlines:\n")
    for entry in all_entries:
        print(f"Title: {entry['title']}")
        print(f"Link: {entry['link']}")
        print(f"Summary: {entry['summary'][:200]}...")  # Truncate summary
        print(f"Published: {entry['published']}")
        print("-" * 50)

if __name__ == "__main__":
    aggregate_news()