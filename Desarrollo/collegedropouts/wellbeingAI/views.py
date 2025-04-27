from django.shortcuts import render
from django.views import View
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import *
from .models import *
from .serializers import *
import requests
from django.core.files.storage import FileSystemStorage
import google.generativeai as genai
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

genai.configure(api_key="Gemini api key")

model = genai.GenerativeModel('gemini-1.5-pro')


@method_decorator(csrf_exempt, name='dispatch')
class IndexTestView(View):
    template_name = 'pages/index.html'

    def get(self, request):
        uris = request.session.get('uploaded_contents', [])
        resumen = request.session.get('generated_summary', '')
        return render(request, self.template_name, {
            'uris': uris,
            'resumen': resumen,
        })

    def post(self, request):
        try:
            model = genai.GenerativeModel('gemini-1.5-pro')  # Ahora siempre lo inicializas

            if request.content_type == 'application/json':
                data = json.loads(request.body)
                action = data.get('action')

                if action == 'generate_summary':
                    uploaded_contents = request.session.get('uploaded_contents', [])
                    if not uploaded_contents:
                        return JsonResponse({'error': 'No contents found to process.'}, status=400)

                    # Armar el prompt concatenando todos los contenidos
                    prompt = " ".join(uploaded_contents)
                    prompt += " Based on the information, identify students at risk of dropping out due to low attendance or low grades, and suggest possible action plans."

                    response = model.generate_content([prompt])
                    
                    summary = response.text
                    request.session['generated_summary'] = summary

                    return JsonResponse({'summary': summary})

            else:
                # Procesar subida de archivos
                uploaded_files = request.FILES.getlist('file')
                uploaded_contents = []

                for uploaded_file in uploaded_files:
                    content = uploaded_file.read().decode('utf-8')  # Leer archivo como texto
                    uploaded_contents.append(content)

                request.session['uploaded_contents'] = uploaded_contents
                request.session['generated_summary'] = ''

                return JsonResponse({'message': 'Files uploaded successfully'})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
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