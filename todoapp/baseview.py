from rest_framework.decorators import api_view
from rest_framework.response import Response


# HOME VIEW
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'admin_panel': 'admin/',
        'all_tasks': 'tasks/getList',
        'get_specific_task': 'tasks/<id>/getOne',
        'add_new_task': 'tasks/create',
        'edit_one_task': 'tasks/<id>/edit',
        'drop_one_task': 'tasks/<id>/drop'
    }
  
    return Response(api_urls)
