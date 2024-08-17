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
