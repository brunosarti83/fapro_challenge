from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils.uf_scraper_sd import get_uf
from .utils.uf_scraper_month import get_uf_month

@api_view(['GET'])
def uf_single_date_view(request, fecha):
    try:
        processed_data = get_uf(datestring=fecha)
        return Response(processed_data, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=400)
    
@api_view(['GET'])
def uf_month_view(request, mes, anio):
    try:
        processed_data = get_uf_month(month=mes, year=anio)
        return Response(processed_data, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=400)