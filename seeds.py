import json

from models import Author, Quotes, Tag
import connect

# Add to MongoDB collection 'authors'
authors_dict = {}
with open("authors.json", "r") as file:
    authors = json.load(file)
for item in authors:
    authors_dict[item["fullname"]] = Author(
        fullname=item["fullname"],
        born_date=item["born_date"],
        born_location=item["born_location"],
        description=item["description"],
    ).save()

# Add to MongoDB collection 'quotes'
with open("quotes.json", "r") as file:
    quotes = json.load(file)
for item in quotes:
    tags = [Tag(name=tag) for tag in item["tags"]]
    Quotes(
        tags=tags,
        author=authors_dict[item["author"]],
        quote=item["quote"],
    ).save()


# for k, v in authors_dict.items():
#     print(k, v["id"])