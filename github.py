
##### this code will get input and extract the github username

#will use the re module
import re
##input collection'

url = input(" Please enter your URL: ").strip()


if matches := re.search(r"^(?:https?://)?(?:www\.)?github\.com/([a-z0-9_]+)$",url, re.IGNORECASE):
    print(f"WELCOME:", matches.group(1))












    