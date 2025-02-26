# this code is for practice extracting the username  from url

#we will use the re module to be able to do this

import re

# then we get the user input

url = input(" Please enter you url: ").strip()

#then we do the extraction operation on the data 

if  matches := re.search(r"^(?:https?://)?(?:www\.)?google\.com/([a-z0-9_]+)$",url,re.IGNORECASE):
    print(f"Your username is : ", matches.group(1))