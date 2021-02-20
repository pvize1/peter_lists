import pytest

from django.test import TestCase
from django.urls import reverse

from .factories import UserFactory
from .factories import BookFactory, book
from ..models import Book
from ..views import BookListView, BookDetailView

pytestmark = pytest.mark.django_db


@pytest.fixture
def user():
    return UserFactory()

def test_good_cheese_list_view_expanded(rf):
    url = reverse("books:list")
    request = rf.get(url)
    callable_obj = BookListView.as_view()
    response = callable_obj(request)
    TestCase.assertContains(response, "Book List")


def test_good_book_list_view(rf):
    # Get the request
    request = rf.get(reverse("books:list"))
    # Use the request to get the response
    response = BookListView.as_view()(request)
    # Test that the response is valid
    TestCase.assertContains(response, "Book List")


def test_good_book_detail_view(rf, book):
    url = reverse("books:detail", kwargs={"slug": book.slug})
    request = rf.get(url)
    callable_obj = BookDetailView.as_view()
    response = callable_obj(request, slug=book.slug)
    TestCase.assertContains(response, book.title)


def test_good_book_create_view(client, user):
    client.force_login(user)
    url = reverse("books:add")
    response = client.get(url)
    assert response.status_code == 200


def test_book_list_contains_2_books(rf):
    book1 = BookFactory()
    book2 = BookFactory()
    request = rf.get(reverse("books:list"))
    response = BookListView.as_view()(request)
    TestCase.assertContains(response, book1.title)
    TestCase.assertContains(response, book2.title)


def test_detail_contains_book_data(rf):
    book = BookFactory()
    url = reverse("books:detail", kwargs={"slug": book.slug})
    request = rf.get(url)
    callable_obj = BookDetailView.as_view()
    response = callable_obj(request, slug=book.slug)
    TestCase.assertContains(response, book.title)
    TestCase.assertContains(response, book.subtitle)
    TestCase.assertContains(response, book.author.name)
    TestCase.assertContains(response, book.publisher.name)

def test_book_create_form_valid(client, user):
    client.force_login(user)
    form_data = {
        "title": "Good Book",
        "description": "A Really Good Book",
    }
    url = reverse("books:add")
    response = client.post(url, form_data)
    assert response.status_code == 302

    book = Book.objects.get(title="Good Book")
    assert book.description == "A Really Good Book"
    assert book.creator == user
