#extrating the user name from a url
import re

url = input( "URL : ").strip()



if matches := re.search(r"^(?:https?://)?(?:www\.)?twiter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username: " , matches.group(1))

# username = re.sub(r"^(https?://)?(www\.)?twiter\.com/", "", url)
# print(f"Username: {username}")










# url = input( "URL : ").strip()

# username = url.removeprefix("https://twitter.com/", "")

# print(f"{username}")
