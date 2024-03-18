from datetime import datetime

from mongoengine import EmbeddedDocument, Document
from mongoengine.fields import (
    Document,
    DateTimeField,
    EmbeddedDocumentField,
    ListField,
    StringField,
    ReferenceField,
)


class Tag(EmbeddedDocument):
    name = StringField()


class Author(Document):
    fullname = StringField()
    born_date = DateTimeField(default=datetime.now())
    born_location = StringField()
    description = StringField()


class Quotes(Document):
    tags = ListField(EmbeddedDocumentField(Tag))
    author = ReferenceField("Author")
    quote = StringField()