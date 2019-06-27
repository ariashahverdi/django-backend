from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        ''' Test Creating a new user with an email is sucessful '''
        email = 'test@testing.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalize(self):
        ''' Test the email for new user is normalized '''
        email = 'test@TESTING.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='password'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        ''' Test creating user with no email raises error '''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'password')

    def test_create_new_superuser(self):
        ''' Test Creating a new superuser '''
        user = get_user_model().objects.create_superuser(
            email='test@testing.com',
            password='password'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
