from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils.uf_scraper import get_uf

@api_view(['GET'])
def uf_single_date_view(request, datestring):
    try:
        processed_data = get_uf(datestring)
        return Response(processed_data, status=200)
    except Exception as e:
        return Response({'error': str(e)}, status=400)