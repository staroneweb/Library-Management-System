import pytest
from rest_framework import status
from books.models import Book
from rest_framework_simplejwt.tokens import RefreshToken


def auth_client(client, user):
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return client


@pytest.mark.django_db
def test_admin_can_create_book(api_client, create_admin):
    admin = create_admin()
    client = auth_client(api_client, admin)

    response = client.post("/api/books/", {
        "title": "Clean Code",
        "author": "Robert Martin",
        "isbn": "9780132350884",
        "page_count": 464,
        "is_available": True
    }, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert Book.objects.count() == 1


@pytest.mark.django_db
def test_user_cannot_create_book(api_client, create_user):
    user = create_user()
    client = auth_client(api_client, user)

    response = client.post("/api/books/", {
        "title": "Not Allowed",
        "author": "Test",
        "isbn": "1111",
        "page_count": 10
    }, format="json")

    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_anyone_can_view_books(api_client):
    response = api_client.get("/api/books/")
    assert response.status_code == status.HTTP_200_OK
