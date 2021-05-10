# there are nay way  to parse the URL with parameters


# ---1---
from urllib.parse import urlsplit, parse_qs

url = "http://www.example.org/default.html?ct=32&op=92&item=98"
query = urlsplit(url).query
params = parse_qs(query)

#>>> params
#{'item': ['98'], 'op': ['92'], 'ct': ['32']}
#>>> dict(params)
#{'item': ['98'], 'op': ['92'], 'ct': ['32']}
#>>> {k: v[0] for k, v in params.items()}
#{'item': '98', 'op': '92', 'ct': '32'}

# ---or shortly---
from urllib import parse
params = dict(parse.parse_qsl(parse.urlsplit(url).query))

# --2--
url = "http://www.example.org/default.html?ct=32&op=92&item=98"
url = url.split("?")[1]
dict = {x[0] : x[1] for x in [x.split("=") for x in url[1:].split("&") ]}
