import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if url := re.search(r".*src=\"(https?://(?:www.)?youtube.com/embed/(\w*))\".*", s, re.IGNORECASE):
        youtube_url = url.group(1)
        if "https" not in youtube_url:
            youtube_url = youtube_url.replace("http", "https")
        if "www" in youtube_url:
            youtube_url = youtube_url.replace("www.", "")
        youtube_url = youtube_url.replace("be.com/embed", ".be")
        return youtube_url
    else:
        return None


if __name__ == "__main__":
    main()
