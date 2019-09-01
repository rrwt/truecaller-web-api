from django.test import TestCase
from django.urls import resolve
from django.template.loader import render_to_string

from home.views import home_page


class HomePageTest(TestCase):
    def test_can_resolve_to_home_page_url_view(self):
        found = resolve("/")
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get("/")
        html = response.content.decode("utf8")

        self.assertIn("<html>", html)
        self.assertIn("<title>Truecaller</title>", html)
        self.assertTrue(html.endswith("</html>"))

    def test_home_url_uses_home_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_can_save_a_post_request(self):
        response = self.client.post("/", data={"phone_number": "5215544975736"})
        self.assertIn("requestId", response.content.decode())
