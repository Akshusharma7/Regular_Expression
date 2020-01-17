import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

subbed_urls = pattern.sub(r'\2\3', urls)

print(subbed_urls)

# matches = pattern.finditer(urls)
'''
Group 0 - full urls
Group 1 - www urls part
Group 2 - doman name like google etc
Group 3 - like .com, .net, .gov etc
# for match in matches:
#     print(match.group(3))
