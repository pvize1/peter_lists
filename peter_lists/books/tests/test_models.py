import pytest

from django.template.defaultfilters import slugify
from .. import views

from peter_lists.books.tests.factories import (
    BookFactory,
    AuthorFactory,
    PublisherFactory,
    BookTypeFactory,
)

pytestmark = pytest.mark.django_db


def test_author__str__():
    author = AuthorFactory()
    assert author.__str__() == author.name
    assert str(author) == author.name


def test_publisher__str__():
    publisher = PublisherFactory()
    assert publisher.__str__() == publisher.name
    assert str(publisher) == publisher.name


def test_booktype__str__():
    booktype = BookTypeFactory()
    assert booktype.__str__() == booktype.type
    assert str(booktype) == booktype.type


def test_book__str__():
    book = BookFactory()
    assert book.__str__() == book.title
    assert str(book) == book.title


def test_book_save():
    book = BookFactory(slug="_")
    assert book.slug == slugify(book.title)


def test_get_absolute_url():
    book = BookFactory()
    url = book.get_absolute_url()
    assert url == f"/books/{book.slug}/"
