from django.test import TestCase


class TestViews(TestCase):
    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")
    
    def test_logout_user(self):
        page = self.client.get("/logout")
        self.assertTrue(page.status_code, 200)
        self.assertTemplateNotUsed(page, "index.html")
    
    def test_login_user(self):
        page = self.client.get("/login/{0}".format(id))
        self.assertTrue(page.status_code, 200)
        self.assertTemplateNotUsed(page, "index.html")
        
    def test_registration_user(self):
        page = self.client.get("/registration/1")
        self.assertEqual(page.status_code, 404)
        
    def test_profile_user(self):
        page = self.client.get("/profile/1")
        self.assertEqual(page.status_code, 404)