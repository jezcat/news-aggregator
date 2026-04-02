import feedparser
from colorama import init, Fore, Style
import socket
from bs4 import BeautifulSoup  # NEW

# Initialize colorama
init(autoreset=True)

# Set timeout for RSS requests
socket.setdefaulttimeout(5)  # max 5 seconds per site

# Toggle to show all headlines, ignoring keywords
SHOW_ALL = False  # Set True to display every headline

# Keywords to filter important news
KEYWORDS = [
    "war", "election", "ai", "space", "quantum", "china", "us", "breaking", "military", "defense",
    "news", "world", "nasa", "technology", "tech", "stocks", "russia", "climate", "policy",
    "protest", "market", "business", "live", "update", "trending", "urgent", "exclusive",
    "crisis", "alert", "viral", "scandal", "conflict", "investigation", "crime", "corruption",
    "economy", "inflation", "weather", "disaster", "healthcare", "education", "innovation",
    "security", "political", "controversial"
]

# RSS feeds: name -> (URL, description)
feeds = {
    "CNN": ("http://rss.cnn.com/rss/edition.rss", "Trusted global news outlet"),
    "CBC": ("https://www.cbc.ca/cmlink/rss-topstories", "Canada's national broadcaster"),
    "Guardian": ("https://www.theguardian.com/world/rss", "International news and opinion"),
    "Google News": ("https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en", "Aggregated top news"),
    "SpaceQ": ("https://spaceq.ca/feed/", "Space and satellite news"),
    "Quantum Insider": ("https://thequantuminsider.com/feed/", "Quantum technology news"),
    "The Debrief": ("https://thedebrief.org/feed/", "Defense, intelligence, and aerospace news"),
    "Defense Scoop": ("https://defensescoop.com/feed/", "US defense news"),
    "NewsNation": ("https://www.newsnationnow.com/rss/", "US national news"),
    "Space.com": ("https://www.space.com/feeds/all", "Space exploration and astronomy"),
    "Ars Technica": ("https://feeds.arstechnica.com/arstechnica/index", "Tech news and analysis"),
    "Reuters": ("https://www.reutersagency.com/feed/?best-topics=top-news", "Global news and finance"),
    "Defense News": ("https://www.defensenews.com/digital-edition/feed/", "Global military news"),
    "Military Times": ("https://www.militarytimes.com/rss/all-news/", "Military news for US armed forces"),
    "Global News": ("https://globalnews.ca/feed/", "Canadian national news"),
    "Channel News Asia": ("https://www.channelnewsasia.com/rssfeeds/8395986", "Southeast Asia news"),
    "The Intercept": ("https://theintercept.com/feed/?cat=47", "Investigative journalism"),
    "The Hill": ("https://thehill.com/rss/syndicator/19110", "US politics and policy news"),
    "Wired": ("https://www.wired.com/feed/rss", "Technology, science, and culture"),
    "Bellingcat": ("https://www.bellingcat.com/feed/", "Open-source investigative journalism"),
    "InfoWorld": ("https://www.infoworld.com/category/news/index.rss", "IT and developer news"),
}

# Color mapping for sites
SITE_COLORS = [
    Fore.CYAN, Fore.MAGENTA, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.RED
]

def is_important(title):
    return SHOW_ALL or any(word.lower() in title.lower() for word in KEYWORDS)

# NEW: Clean HTML summaries
def clean_html(raw_html):
    if not raw_html:
        return ""
    soup = BeautifulSoup(raw_html, "html.parser")
    text = soup.get_text(separator=" ", strip=True)
    # Limit to 400 chars for console readability
    return text[:400] + ("..." if len(text) > 400 else "")

def get_news():
    seen = set()
    important_news = []

    for i, (name, (url, desc)) in enumerate(feeds.items()):
        color = SITE_COLORS[i % len(SITE_COLORS)]
        print(f"{color}Checking {name}...{Style.RESET_ALL}")

        if not url:
            print(f"Skipping {name} (no RSS feed)")
            continue

        try:
            feed = feedparser.parse(url)

            for entry in feed.entries[:5]:  # top 5 headlines per site
                title = entry.title
                link = entry.link
                summary = getattr(entry, "summary", "")

                if title not in seen:
                    seen.add(title)
                    if is_important(title):
                        important_news.append({
                            "site": name,
                            "site_color": color,
                            "description": desc,
                            "title": title,
                            "summary": clean_html(summary),
                            "link": link
                        })

        except Exception as e:
            print(f"Skipped {name} (error: {e})")

    return important_news

def main():
    news = get_news()

    print("\n" + "="*80)
    print(f"{Style.BRIGHT}IMPORTANT NEWS:{Style.RESET_ALL}")
    print("="*80 + "\n")

    if not news:
        print("No major headlines found.")
    else:
        for item in news:
            # Big colored site header
            print(f"{item['site_color']}{Style.BRIGHT}{item['site']}{Style.RESET_ALL}")
            print(f"{Style.BRIGHT}{item['title'].upper()}{Style.RESET_ALL}")
            # Summary
            if item['summary']:
                print(item['summary'])
            # Link
            print(f"Read more: {item['link']}\n")
            print("-" * 80)

if __name__ == "__main__":
    main()
