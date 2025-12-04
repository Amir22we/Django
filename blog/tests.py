from django.test import SimpleTestCase, Client
from django.views.generic import TemplateView

from . import views

class HomePageGetTests(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        url = '/'
        client = Client()
        cls.response = client.get(url)

    def test_url_access(self):
        self.assertEqual(self.response.status_code, 200)

    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name, 'home')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, 'blog')

    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func, views.index)

    
    def test_template_name(self):
        self.assertTemplateUsed(self.response, 'blog/index.html')

    def test_base_template_name(self):
        self.assertTemplateUsed(self.response, 'base.html')

    def test_context_var(self):
        self.assertIn('site', self.response.context)
        self.assertEqual(self.response.context['site'], 'mysite.com')

class AboutPageGetTests(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        url = '/about/'
        client = Client()
        cls.response = client.get(url)
            
    def test_url_access(self):
        self.assertEqual(self.response.status_code, 200)

    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name, 'about')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, 'blog')
    
    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func.view_class, TemplateView)

    
    def test_template_name(self):
        self.assertTemplateUsed(self.response, 'blog/about.html')

    def test_base_template_name(self):
        self.assertTemplateUsed(self.response, 'base.html')

    def test_context_var(self):
        self.assertIn('site', self.response.context)
        self.assertEqual(self.response.context['site'], 'mysite.com')
class ContactPageGetTest(SimpleTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        url = '/contact/'
        client = Client()
        cls.response = client.get(url)

    def test_url_access(self):
        self.assertEqual(self.response.status_code, 302)

    def test_url_name(self):
        self.assertEqual(self.response.resolver_match.url_name, 'contact')

    def test_url_namespace(self):
        self.assertEqual(self.response.resolver_match.namespace, 'blog')

    def test_view_name(self):
        self.assertEqual(self.response.resolver_match.func, views.contact)

    
    def test_redirect_url(self):
        self.assertRedirects(self.response, '/about/')

    

