import pytest
from rest_framework.test import APIClient
from accounts.models import Account


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user(db):
    def make_user(**kwargs):
        return Account.objects.create_user(
            email=kwargs.get("email", "user@test.com"),
            username=kwargs.get("username", "testuser"),
            first_name="Test",
            last_name="User",
            password=kwargs.get("password", "strongpassword"),
            role="user"
        )
    return make_user


@pytest.fixture
def create_admin(db):
    def make_admin(**kwargs):
        return Account.objects.create_superuser(
            email=kwargs.get("email", "admin@test.com"),
            username=kwargs.get("username", "admin"),
            first_name="Admin",
            last_name="User",
            password=kwargs.get("password", "adminpass"),
        )
    return make_admin
