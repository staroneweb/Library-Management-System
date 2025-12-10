import pytest
from rest_framework import status
from books.models import Book
from rest_framework_simplejwt.tokens import RefreshToken


def auth_client(client, user):
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return client


@pytest.mark.django_db
def test_user_can_borrow_book(api_client, create_user):
    user = create_user()
    client = auth_client(api_client, user)

    book = Book.objects.create(
        title="Django Test",
        author="Tester",
        isbn="9999",
        page_count=100,
        is_available=True
    )

    response = client.post("/api/loans/borrow/", {
        "book_id": book.id
    }, format="json")

    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_user_can_return_book(api_client, create_user):
    user = create_user()
    client = auth_client(api_client, user)

    book = Book.objects.create(
        title="Return Book",
        author="Tester",
        isbn="8888",
        page_count=150,
        is_available=True
    )

    client.post("/api/loans/borrow/", {"book_id": book.id}, format="json")

    response = client.post("/api/loans/return/", {
        "book_id": book.id
    }, format="json")

    assert response.status_code == status.HTTP_200_OK
