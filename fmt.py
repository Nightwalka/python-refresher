
import re

name = input("whats your name: ").strip()


if matches:= re.search(r"^(.+), *(.+)$",name):
    name = matches.group(2) + " " + matches.group(1)


print(f"Hello: {name}")


# matches = re.search(r"^(.+), (.+)$",name)
# matches = re.search(r"^(.+), ?(.+)$",name)

# matches = re.search(r"^(.+), *(.+)$",name)

# if matches:
#     name = matches.group(2) + " " + matches.group(1)



    # name = f"{first} {last}"
# if "," in name:
#     last, first =name.split(", ")
#     name = f"{first} {last}"