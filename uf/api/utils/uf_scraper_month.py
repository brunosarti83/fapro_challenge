from datetime import datetime
from typing import List

import requests
from bs4 import BeautifulSoup


def get_uf_month(month: str, year: str) -> List:
  '''
  Obtiene UF del mes completo.
  '''  
  try:
    year_int = int(year)
  except ValueError:
    raise Exception('Año debe ser un valor de 2013 en adelante')

  if year_int < 2013:
    raise Exception('Año debe ser un valor de 2013 en adelante')

  try:
    month_int = int(month)
  except ValueError:
    raise Exception('Mes debe ser un valor de 1 a 12')

  if month_int < 1 or month_int > 12:
    raise Exception('Mes debe ser un valor de 1 a 12')

  # Descargar todo el html de la página para el año solicitado
  response = requests.get(f'https://www.sii.cl/valores_y_fechas/uf/uf{year}.htm')

  # Validar respuesta status OK
  if response.status_code != 200:
    raise Exception(f"Página no encontrada, status: {response.status_code}")

  # Parsear el html con BeautifulSoup
  soup = BeautifulSoup(response.text, 'lxml')

  rows = soup.find('table', id='table_export').find_all('tr')
  if len(rows) == 0:
    raise Exception(
        f"No se puedo encontrar valores para el mes {month} del año {year}")

  # Preparar los datos
  data = []

  # Iterar las filas (salvo primera: 'Ene', 'Feb', 'Mar', etc) y extraer la UF
  for row in rows[1:]:
    day = row.find('th').text
    # Validar fecha para evitar 30 de febrero
    try:
      date = datetime.strptime(f'{day}-{month}-{year}', '%d-%m-%Y')
    except ValueError:
      continue

    uf_value = row.find_all('td')[month_int - 1].text.replace('.', '').replace(',', '.')
    data.append({
        'fecha': f'{day}-{month_int}-{year_int}',
        'valor_uf': 'no disponible' if uf_value == '\xa0' else float(uf_value)
    })

  return data