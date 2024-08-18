from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class SingleDateUFTest(APITestCase):

    def test_get_single_date_uf(self):

        test_cases = [
            { 'datestring': '02-06-2023', 'uf_value': 36039.85 },
            { 'datestring': '08-08-2014', 'uf_value': 24068.48 },
            { 'datestring': '04-06-2018', 'uf_value': 27088.79 },
        ]

        for case in test_cases:
            with self.subTest(case=case):
                url = reverse('uf_single_date_view', kwargs={'fecha': case['datestring']})
                response = self.client.get(url)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(response.data['valor_uf'], case['uf_value'])
    
    def test_get_uf_month(self):
        test_cases = [
            { 'month': '6', 'year': '2023', 'index': 10, 'date': '11-6-2023', 'uf_value': 36066.64 },
            { 'month': '4', 'year': '2021', 'index': 15, 'date': '16-4-2021', 'uf_value': 29439.24 },
        ]

        for case in test_cases:
            with self.subTest(case=case):
                url = reverse('uf_month_view')
                response = self.client.get(f"{url}?mes={case['month']}&anio={case['year']}")
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                self.assertEqual(response.data[case['index']]['fecha'], case['date'])
                self.assertEqual(response.data[case['index']]['valor_uf'], case['uf_value'])
