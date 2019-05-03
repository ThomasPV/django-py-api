from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelsTest(TestCase):

    def test_create_user_email(self):
        email = "abc@gmail.com"
        password = "12345"
        phone = "9292929292"

        user = get_user_model().objects.create_user(
            email=email,
            phone = phone ,
            password = password
           
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_check_email(self):
            email = "abc@Gmail.com"
            password = "12345"
            phone = 0

            user = get_user_model().objects.create_user(
                email=email,
                phone = phone ,
                password = password
                
            )

            self.assertEqual(user.email,email.lower())
            self.assertRaises(ValueError)

    def test_create_super_user(self):
        """Create A Super User"""

        user = get_user_model().objects.create_superuser(
            'abc_superuser@gmail.com',
            '12345'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

   