# users/tests.py
from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
class CustomUserTests(TestCase):


    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='md_test_user',
            email='md_test_user@email.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'md_test_user')
        self.assertEqual(user.email, 'md_test_user@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
        username='md_test_superuser',
        email='md_test_superuser@email.com',
        password='testpass123'
        )
        self.assertEqual(admin_user.username, 'md_test_superuser')
        self.assertEqual(admin_user.email, 'md_test_superuser@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)