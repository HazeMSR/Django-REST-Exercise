import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create():
	user = User.objects.create_user('test', 'test@test.com', 'test')
	count = User.objects.all().count()
	print('Your current count is:', count)
	assert User.objects.count() == 1
	user.delete()

@pytest.mark.django_db
def test_no_user():
	count = User.objects.all().count()
	print(count)
	assert User.objects.count() == 0

@pytest.fixture
def user_1(db):
	return User.objects.create_user('test-user')

@pytest.mark.django_db
def test_set_check_password(user_2):
	user_2.set_password('new-password')
	print('This is my user name:',user_2)
	assert user_2.check_password('new-password') is True
	user_2.delete()

def test_new_user(new_user):
	print(new_user.first_name)
	assert new_user.first_name == 'MyName'
	