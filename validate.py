import re

email = input("wha's your email?").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$",email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")












  



# import re

# email = input("wha's your email?").strip()

# if re.search(r"^[^@]+@[^@]+\.edu$",email):
#     print("valid")
# else:
#     print("invalid")


# import re

# email = input("wha's your email?").strip()

# if re.search(r"^[a-zA-Z]+@[a-zA-Z]+\.edu$",email):
#     print("valid")
# else:
#     print("invalid")