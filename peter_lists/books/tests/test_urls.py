import pytest

from django.urls import reverse, resolve

from .factories import BookFactory

pytestmark = pytest.mark.django_db


@pytest.fixture
def book():
    return BookFactory()


def test_list_reverse():
    """ books:list should reverse to /books/."""
    assert reverse("books:list") == "/books/"


def test_list_resolve():
    """/books/ should resolve to books:list."""
    assert resolve("/books/").view_name == "books:list"


def test_add_reverse():
    """ books:add should reverse to /books/add/."""
    assert reverse("books:add") == "/books/add/"


def test_add_resolve():
    """/books/add/ should resolve to books:add."""
    assert resolve("/books/add/").view_name == "books:add"


def test_detail_reverse(book):
    """ books:detail should reverse to /books/bookslug/."""
    url = reverse("books:detail", kwargs={"slug": book.slug})
    assert url == f"/books/{book.slug}/"


def test_detail_resolve(book):
    """/books/bookslug/ should resolve to books:detail."""
    url = f"/books/{book.slug}/"
    assert resolve(url).view_name == "books:detail"
