import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_user_registration(api_client):
    url = "/api/auth/register/"
    data = {
        "email": "user1@test.com",
        "username": "user1",
        "first_name": "User",
        "last_name": "One",
        "password": "testpass123"
    }

    response = api_client.post(url, data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    assert "access" in response.data
    assert "refresh" in response.data


@pytest.mark.django_db
def test_user_login(api_client, create_user):
    user = create_user()

    url = "/api/auth/login/"
    data = {
        "email": user.email,
        "password": "strongpassword"
    }

    response = api_client.post(url, data, format="json")

    assert response.status_code == status.HTTP_200_OK
    assert "access" in response.data
