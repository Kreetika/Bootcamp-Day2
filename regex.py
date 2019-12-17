# import re

# pattern = r'\d+'

# sequence = 'asdf777ghjkl9hsdjkjsdj6'

# print(re.findall(pattern,sequence))

#..................................................
# import re

# pattern = r'\w+@\w+\.\w+'

# sequence = 'ahsahsjsdhdgsjd kreetikabaral@gmail.com sajkjdsjkdksdkj'

# print(re.findall(pattern,sequence))

#..................................
pattern = r'\w+@\w+\.\w+'

sequence = 'ahsahsjsdhdgsjd kreetikabaral@gmail.com sajkjdsjkdksdkj'

print(re.findall(pattern,sequence))


