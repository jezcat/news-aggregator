# News Aggregator

A Python script that scans multiple news sites and aggregates the latest headlines and articles.

Created by jezcat.

## Features

- Scans multiple news websites
- Aggregates headlines and summaries
- Supports customizable sources
- Outputs results in a readable format

## News Sources

| Site Name | RSS / Feed URL | Description |
|-----------|----------------|------------|
| CNN | [RSS](http://rss.cnn.com/rss/edition.rss) | Trusted global news outlet |
| CBC | [RSS](https://www.cbc.ca/cmlink/rss-topstories) | Canada’s national broadcaster |
| The Guardian | [RSS](https://www.theguardian.com/world/rss) | International news and opinion |
| Google News | [RSS](https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en) | Aggregated top news |
| SpaceQ | [RSS](https://spaceq.ca/feed/) | Space and satellite news |
| Quantum Insider | [RSS](https://thequantuminsider.com/feed/) | Quantum technology news |
| The Debrief | [RSS](https://thedebrief.org/feed/) | Defense, intelligence, and aerospace news |
| Defense Scoop | [RSS](https://defensescoop.com/feed/) | US defense news |
| NewsNation | [RSS](https://www.newsnationnow.com/rss/) | US national news (placeholder RSS) |
| Space.com | [RSS](https://www.space.com/feeds/all) | Space exploration and astronomy |
| Ars Technica | [RSS](https://feeds.arstechnica.com/arstechnica/index) | Tech news and analysis |
| Reuters | [RSS](https://www.reutersagency.com/feed/?best-topics=top-news) | Global news and finance |
| Defense News | [RSS](https://www.defensenews.com/digital-edition/feed/) | Global military news |
| Military Times | [RSS](https://www.militarytimes.com/rss/all-news/) | Military news for US armed forces |
| Global News | [RSS](https://globalnews.ca/feed/) | Canadian national news |
| Channel News Asia | [RSS](https://www.channelnewsasia.com/rssfeeds/8395986) | Southeast Asia news |
| The Intercept | [RSS](https://theintercept.com/feed/?cat=47) | Investigative journalism |
| The Hill | [RSS](https://thehill.com/rss/syndicator/19110) | US politics and policy news |
| Wired | [RSS](https://www.wired.com/feed/rss) | Technology, science, and culture |
| Bellingcat | [RSS](https://www.bellingcat.com/feed/) | Open-source investigative journalism |
| InfoWorld | [RSS](https://www.infoworld.com/category/news/index.rss) | IT and developer news |
| War.gov | None | US Department of War site (no RSS) |
| Janes | None | Defense analysis (subscription required, no RSS) |
| San.com | None | Placeholder site (no RSS) |

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/jezcat/news-aggregator.git
   ```

2. Install dependencies:
   ```
   pip install feedparser
   pip install colorama
   pip install beautifulsoup4
   ```

## Usage

Run the script with:
```
cd news-aggregator
python news.py
```
The script will fetch the latest articles and display them in the console.

Customize the sources by editing the feeds dictionary in the script.

## Customization

### Filtering News Articles by Keywords

You can filter news articles based on keywords you want to see by editing the keyword list inside the script. For example, look for a variable like:

```
KEYWORDS = ['quantum', 'space', 'defense']
```

Add the keywords you want to include.

The script will only show articles whose titles contain at least one of these keywords (case-insensitive).

To see all articles regardless of keywords, set the keyword list to empty (`KEYWORDS = []`) or enable a `SHOW_ALL` flag if your script has one.

### Adding or Removing News Sources

To customize which news sites are scanned, edit the `FEEDS` dictionary inside the script:

```
FEEDS = {
    'CNN': ('http://rss.cnn.com/rss/edition.rss', 'Trusted global news outlet'),
    'New Site': ('https://example.com/rss', 'Description of the new site'),
    # Add or remove sites here
}
```

To add a new source, add a new entry with the site name, RSS feed URL, and a short description.

To remove a source, simply delete or comment out its entry.

If a site has no RSS feed, use `None` as the URL, but those sources will be skipped unless you implement custom scraping.

## Requirements

- Python 3.8+
- Libraries listed in requirements.txt (e.g., feedparser)

## Contributing

Feel free to submit issues and pull requests. 
