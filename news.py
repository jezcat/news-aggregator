import feedparser
import socket

socket.setdefaulttimeout(5)  # max 5 seconds per site

# Toggle to show all headlines, ignoring keywords
SHOW_ALL = False  # Set True to display every headline

# Original + new keywords
KEYWORDS = [
    # Original keywords
    "war", "election", "ai", "space", "quantum", "china", "us", "breaking", "military", "defense",
    
    # New extended keywords
    "news", "world", "nasa", "new", "technology", "tech", "stocks", "international", "russia",
    "uap", "hearing", "climate", "policy", "protest", "results", "market", "business",
    "live", "update", "trending", "urgent", "exclusive", "crisis", "alert", "viral",
    "trend", "shocking", "poll", "legislature", "scandal", "coalition", "candidate", "verdict",
    "bipartisan", "administration", "DOD", "fbi", "cia", "allegation", "conflict", "probe",
    "investigation", "crime", "charge", "charges", "accused", "scam", "corruption", "violation",
    "hostile", "dispute", "rumor", "economy", "inflation", "weather", "disaster", "revenue",
    "bankruptcy", "investment", "unemployment", "employment", "startup", "healthcare", "education",
    "sustainability", "epidemic", "health", "diversity", "innovation", "rights", "security",
    "criminal", "invention", "CEO", "political", "politician", "controversial"
]

# feed dictionary: name -> (RSS link, description)
feeds = {
    "CNN": ("http://rss.cnn.com/rss/edition.rss", "Trusted global news outlet"),
    "CBC": ("https://www.cbc.ca/cmlink/rss-topstories", "Canada's national broadcaster"),
    "Guardian": ("https://www.theguardian.com/world/rss", "International news and opinion"),
    "Google News": ("https://news.google.com/rss?hl=en-US&gl=US&ceid=US:en", "Aggregated top news"),
    "SpaceQ": ("https://spaceq.ca/feed/", "Space and satellite news"),
    "Quantum Insider": ("https://thequantuminsider.com/feed/", "Quantum technology news"),
    "The Debrief": ("https://thedebrief.org/feed/", "Defense, intelligence, and aerospace news"),
    "Defense Scoop": ("https://defensescoop.com/feed/", "US defense news"),
    "NewsNation": ("https://www.newsnationnow.com/rss/", "US national news"),  # placeholder RSS
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
    # Sites without RSS: placeholders, may need HTML scraping later
    "War.gov": (None, "US Department of War site (no RSS)"),
    "Janes": (None, "Defense analysis (subscription required)"),
    "San.com": (None, "Placeholder site, no RSS found")
}

def is_important(title):
    return any(word in title.lower() for word in KEYWORDS)

def get_news():
    seen = set()
    important_news = []

    for name, (url, desc) in feeds.items():
        print(f"Checking {name}...")  # show progress
        if not url:
            print(f"Skipping {name} (no RSS feed)")
            continue

        try:
            feed = feedparser.parse(url)

            for entry in feed.entries[:5]:  # top 5 headlines per site
                title = entry.title

                if title not in seen:
                    seen.add(title)
                    if is_important(title):
                        important_news.append(f"[{name}] ({desc}) {title}")

        except Exception as e:
            print(f"Skipped {name} (error)")

    return important_news

def main():
    news = get_news()

    print("\nIMPORTANT NEWS:\n")

    if not news:
        print("No major headlines found.")
    else:
        for item in news:
            print(item)

if __name__ == "__main__":
    main()