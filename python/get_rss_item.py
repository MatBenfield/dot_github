"""
 Get RSS
"""
import re
import os
import feedparser
import pathlib

root = pathlib.Path(__file__).parent.resolve()

def replace_chunk(content, marker, chunk):
    replacer = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    chunk = "<!-- {} starts -->\n{}\n<!-- {} ends -->".format(marker, chunk, marker)
    return replacer.sub(chunk, content)

def fetch_blog_entries():
    entries = feedparser.parse("[https://domain.tld/feed.xml")["entries"]
    return [
        {
            "title": entry["title"],
            "url": entry["link"].split("#")[0],
            "published": entry["published"].split("T")[0],
        }
        for entry in entries
    ]

if __name__ == "__main__":
    readme = root / "README.md"
    readme_contents = readme.open().read()

    entries = fetch_blog_entries()[:5]
    entries_md = "\n".join(
        ["- [{title}]({url}) - {published}".format(**entry) for entry in entries]
    )

    rewritten = replace_chunk(readme_contents, "blog", entries_md)
    readme.open("w").write(rewritten)
