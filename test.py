from unittest import TestCase
from converter_service import convert
from app import app

class FlaskViewsTests(TestCase):

    def setUp(self):
        """ Stuff to do before every test"""
        self.client= app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """ Checking """
        with self.client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            
    def test_same_value(self):
        """testing same value"""

        with self.client:
            resp = self.client.get('/process', query_string={'currency1': 'usd', 'currency2' :'usd', 'amount':'1'})
            html = resp.get_data(as_text=True)
            self.assertIn('The result is $ 1.0',html)
            self.assertEqual(resp.status_code, 200)

    def test_invalid_amount(self):
        """testing invalid amount"""

        with self.client:
            resp = self.client.get('/process', query_string={'currency1': 'usd', 'currency2' :'usd', 'amount':'abc'},follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertIn('Amount should be float',html)
            self.assertEqual(resp.status_code, 200)


class ConvertServiceTests(TestCase):
  
    def test_invalid_amount(self):
        unit_input="usd"
        unit_output="eur"
        amount="abc"
        result=convert(unit_input,unit_output,amount)
        self.assertEqual(result,{"outcome":"failed","reason":"Amount should be float"})

    def test_invalid_unit_input(self):
        unit_input="usdo"
        unit_output="eur"
        amount="1"
        result=convert(unit_input,unit_output,amount)
        self.assertEqual(result,{"outcome":"failed","reason":"Wrong input on input currency"})

    def test_invalid_unit_output(self):
        unit_input="usd"
        unit_output="eurs"
        amount="1"
        result=convert(unit_input,unit_output,amount)
        self.assertEqual(result,{"outcome":"failed","reason":"Wrong input on output currency"})