from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .models import *
from .serializers import *

class TextFileUploadView(APIView):
    parser_classes = [MultiPartParser,FormParser]
    
    def post(self,request,*args, **kwargs):
        file = request.FILES['file']
        filename = file.name
        
        file_content = file.read().decode('utf-8')
        line_count = len(file_content.splitlines())
        word_count = len(file_content.split())
        character_count = len(file_content)
        
        file_details = TextFileUpload.objects.create(
            filename=filename,
            line_count = line_count,
            word_count = word_count,
            character_count = character_count
        )
        
        serializer = TextFileUploadSerializer(file_details)
        return Response(serializer.data , status=status.HTTP_201_CREATED)
