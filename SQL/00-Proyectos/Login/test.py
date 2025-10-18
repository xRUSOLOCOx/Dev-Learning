import re




      
pattern = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
emails = ["johne2020@xample.peipllo"]
print(re.match(pattern, emails[0]))