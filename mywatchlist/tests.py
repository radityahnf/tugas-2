from django.test import TestCase
from django.test import Client

# Create your tests here.
class WatchlistTest(TestCase):

    def test_mywatchlist(self):
        response  = Client().get('/mywatchlist/')
        self.assertEqual(response.status_code, 200)
    
    def test_mywatchlist_html(self):
        response  = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code, 200)
    
    def test_mywatchlist_json(self):
        response  = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code, 200)
    
    def test_mywatchlist_xml(self):
        response  = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code, 200)

    def test_view_correct_template(self):
        response = self.client.get('/mywatchlist/')
        self.assertTemplateUsed(response, 'watchlist.html')