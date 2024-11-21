from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

articles = soup.find_all(name="tr", class_="athing")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.find(name="span", class_="titleline").getText()
    article_texts.append(text)
    link =  article_tag.find(name="span", class_="titleline").find(name="a").get("href")
    article_links.append(link)

# article_text = article_tag.getText()
# article_link = article_tag.find(name="a").get("href")
article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvote)

index = article_upvote.index(max(article_upvote))
print(f"Title: {article_texts[index]}, Link: {article_links[index]}")



































# with open(file="website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.name)
#
# # print(soup.p)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)