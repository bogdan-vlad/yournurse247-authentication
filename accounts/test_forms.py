from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm


class TestAuthentication(TestCase):
    
    def test_authentication_and_password(self):
        form = UserLoginForm({'name': 'Create tests'})
        self.assertFalse(form.is_valid())
        
    def test_the_password_you_use_is_the_correct_one(self):
        form = UserRegistrationForm({'name': ''})
        self.assertFalse(form.is_valid())
        
