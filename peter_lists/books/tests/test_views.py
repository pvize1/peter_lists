import pytest

from django.test import TestCase
from django.urls import reverse

from .factories import UserFactory
from .factories import BookFactory
from ..models import Book
from ..views import BookListView, BookDetailView

pytestmark = pytest.mark.django_db


class SimpleTest(TestCase):
    def test_good_book_list_view(self):
        response = self.client.get("/books/")
        self.assertContains(response, "Book List")

    def test_good_book_detail_view(self):
        book = BookFactory()
        url = reverse("books:detail", kwargs={"slug": book.slug})
        response = self.client.get(url)
        self.assertContains(response, book.title)

    def test_good_book_create_view(self):
        user = UserFactory()
        self.client.force_login(user)
        url = reverse("books:add")
        response = self.client.get(url)
        assert response.status_code == 200

    def test_book_list_contains_2_books(self):
        book1 = BookFactory()
        book2 = BookFactory()
        response = self.client.get(reverse("books:list"))
        self.assertContains(response, book1.title)
        self.assertContains(response, book2.title)

    def test_detail_contains_book_data(self):
        book = BookFactory()
        url = reverse("books:detail", kwargs={"slug": book.slug})
        response = self.client.get(url)
        self.assertContains(response, book.title)
        self.assertContains(response, book.subtitle)
        self.assertContains(response, book.author.name)
        self.assertContains(response, book.publisher.name)


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
