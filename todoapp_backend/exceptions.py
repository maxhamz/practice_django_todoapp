from rest_framework.views import APIView


class EntryNotFound(APIView):
    status_code = 404
    default_detail = "ENTRY NOT FOUND"
    default_code = "entry_not_found"
