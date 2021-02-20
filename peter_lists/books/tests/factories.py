import pytest

from django.template.defaultfilters import slugify

from factory.django import DjangoModelFactory
from factory import Faker, fuzzy, LazyAttribute, SubFactory
from peter_lists.users.tests.factories import UserFactory

from ..models import Book, Author, Publisher, BookType


class AuthorFactory(DjangoModelFactory):
    class Meta:
        model = Author

    name = fuzzy.FuzzyText()


class PublisherFactory(DjangoModelFactory):
    class Meta:
        model = Publisher

    name = fuzzy.FuzzyText()


class BookTypeFactory(DjangoModelFactory):
    class Meta:
        model = BookType

    type = fuzzy.FuzzyText()


class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    title = fuzzy.FuzzyText()
    subtitle = fuzzy.FuzzyText()
    author = SubFactory(AuthorFactory)
    description = Faker("paragraph", nb_sentences=3, variable_nb_sentences=True)
    isbn = fuzzy.FuzzyText()
    publisher = SubFactory(PublisherFactory)
    pages = 99
    type = SubFactory(BookTypeFactory)
    slug = LazyAttribute(lambda obj: slugify(obj.title))
    creator = SubFactory(UserFactory)


@pytest.fixture
def book():
    return BookFactory()
