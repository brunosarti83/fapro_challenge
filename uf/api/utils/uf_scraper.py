from datetime import datetime
from typing import Dict

import requests
from bs4 import BeautifulSoup


def get_uf(datestring:str) -> Dict:
  
  try:
    date = datetime.strptime(datestring, '%d-%m-%Y')
  except ValueError:
    raise Exception('Formato de fecha inválido. Utilizar DD-MM-YYYY')

  if date < datetime(2013, 1, 1):
    raise Exception('Fecha inválida. Información disponible desde el 01-01-2013')

  day, month, year = datestring.split('-')

  if day[0] == '0':
    day = day[1]
    
  if month[0] == '0':
    month = month[1]
    
  # Descargar todo el html de la página para el año solicitado
  response = requests.get(f'https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm')

  # Validar respuesta status OK
  if response.status_code != 200:
    raise Exception(f"Página no encontrada, status: {response.status_code}")

  # Parsear el html con BeautifulSoup
  soup = BeautifulSoup(response.text, 'lxml')
  
  # Obtener el valor de la UF
  table_row_day = (soup.find('table', id='table_export')
  .find('th', string=day)
  .find_next_siblings('td')
  )

  if len(table_row_day) == 0:
    raise Exception(f"No se pudo encontrar UF para el día {datestring}")

  uf_value = table_row_day[int(month)-1].text.replace('.', '').replace(',', '.')
  
  uf_value = 'no disponible aún' if uf_value == '\xa0' else float(uf_value)
  
  return {
    'fecha': datestring,
    'valor_uf': uf_value
  }