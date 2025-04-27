from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import *
from .models import *
from datetime import date
from .serializers import *

# Create your views here.

class IndexTestView(View):
    template_name = 'pages/index.html'

    def get(self, request):
        return render(request, self.template_name, {})
    
@csrf_exempt
def createclasses(request):
    if request.method == 'POST':    
        try:
            data = JSONParser().parse(request)
            attendance = create_classes(
                start_date_str=data['start_date'],
                weekday=data['weekday'],
                weeks=data['weeks'],
                course_id=data['course_id'],
                start_time=data['start_time'],
                end_time=data['end_time']
            )
            return JsonResponse({'message': 'Classes created successfully', 'id': attendance.id}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)