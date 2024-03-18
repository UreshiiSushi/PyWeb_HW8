# mongodb+srv://mongouser:mongopwd@study.mvlsxeo.mongodb.net/?retryWrites=true&w=majority

import connect
from models import Author, Quotes, Tag


def main():
    while True:
        print()
        command = input(
            "Input command from list: name:author  tag:tag  tags:tag1,tag2... OR exit>>> "
        )
        if "exit" in command:
            break
        if ":" not in command:
            print("Try again")
            continue
        command, arg = command.split(":")
        if command == "name":
            author_id = Author.objects(fullname=arg)
            print(f"All quotes of author {arg}")
            quotes = Quotes.objects(author=author_id[0]["id"])
            for item in quotes:
                print(item.quote)

        elif command == "tag":
            quotes = Quotes.objects(tags__name=arg)
            print(f"All quotes with tag {arg}")
            for item in quotes:
                print(item.quote)

        elif command == "tags":
            quotes = Quotes.objects(tags__name__in=arg.split(","))
            print(f"All quotes with tags {arg}")
            for item in quotes:
                print(item.quote)
        else:
            print("Try again")


if __name__ == "__main__":
    main()