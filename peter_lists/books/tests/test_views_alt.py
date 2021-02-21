import pytest
from pytest_django.asserts import assertContains

from django.urls import reverse


from .factories import UserFactory
from .factories import BookFactory, book
from ..models import Book
from ..views import BookListView, BookDetailView

pytestmark = pytest.mark.django_db


@pytest.fixture
def user():
    return UserFactory()


def test_good_book_list_view_expanded(rf):
    url = reverse("books:list")
    request = rf.get(url)
    callable_obj = BookListView.as_view()
    response = callable_obj(request)
    assertContains(response, "Book List")
