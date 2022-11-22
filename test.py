from unittest import TestCase
from app import app

class FlaskTests(TestCase):

    def setUp(self):
        """ Stuff to do before every test"""
        self.client= app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """ Checking """
        with self.client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            
    def test_redirect(self):
        """testing redirect"""

        # with self.client:
            # resp = self.client.post('/process', data={'first_currency': 'usd', 'final_currency' :'usd', 'amount':'1'})
            # html = resp.get_data(as_text=True)
            # self.assertIn('<p>The result is $ 1.0</p>',html)
            # self.assertIn('')
            # self.assertEqual(resp.status_code, 200)
            # self.assertEqual(resp.location, "http://localhost/")
