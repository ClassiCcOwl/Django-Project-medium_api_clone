import pytest
from core_apps.users.forms import UserCreationForm
from core_apps.users.tests.factories import UserFactory


@pytest.mark.django_db
def test_user_creation_form_valid_data():
    data = {
        "first_name": "John",
        "last_name": "doe",
        "enail": "jown@example.com",
        "password1": "secure_password_1234",
        "password2": "secure_password_1234",
    }
    form = UserCreationForm(data)
    assert form.is_valid()


@pytest.mark.django_db
def test_user_creation_from_invalid_data():
    user = UserFactory()
    data = {
        "first_name": "John",
        "last_name": "doe",
        "enail": user.email,
        "password1": "secure_password_1234",
        "password2": "secure_password_1234",
    }
    form = UserCreationForm(data)
    assert not form.is_valid()
    assert "email" in form.errors
