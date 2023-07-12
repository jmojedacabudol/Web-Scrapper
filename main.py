from bs4 import BeautifulSoup
# import lxml
import requests

response = requests.get(url="https://news.ycombinator.com")
yc_website = response.text

soup = BeautifulSoup(yc_website, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
article_upvotes =[]

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find(name="a").get("href")
    article_links.append(link)

article_id = [score.get('id') for score in
              soup.find_all(name="tr", class_="athing")]


for single_id in article_id:
    try:
        article_upvotes.append(int(soup.find(name="span", id=f"score_{single_id}").getText().split()[0]))

    except AttributeError:
        article_upvotes.append(0)



highest_upvote = article_upvotes.index(max(article_upvotes))

print(article_texts[highest_upvote])
print(article_links[highest_upvote])




# with open("website.html", "r") as data_file:
#     contents = data_file.read()
#
#
# soup = BeautifulSoup(contents, 'html.parser')
#
# # print(soup.title)
# # print(soup.title.name)
# all_anchor_tag = soup.find_all(name="a")
# # print(all_anchor_tag)
#
# # for tag in all_anchor_tag:
#     # print(tag.getText())
#     # print(tag.get("href"))
#
#
# heading = soup.find(name="h1",id="name")
#
# # print(heading)
#
# company_url = soup.select_one(selector="#name")
# print(company_url)
