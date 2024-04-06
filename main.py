import requests
from send_email import send_email

topic="tesla"

api_key="b125cccd88db46678cd1ca8d578bf6c6"
url=f"https://newsapi.org/v2/everything?q={topic}&from=2024-02-04&sortBy=publishedAt&apiKey=b125cccd88db46678cd1ca8d578bf6c6&language=en"


request = requests.get(url)

content = request.json()

body= ""
for article in content["articles"][:20]:
    if article["title"] is not None:
         body= "Subject: Today's news" "\n" + body + article["title"] + "\n" \
         + article["description"] \
         + "\n" + article["url"] + 2*"\n"
body = body.encode("utf-8")
send_email(message = body)


