from rest_framework import serializers
from .models import *

class TextFileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextFileUpload
        fields = ['id','filename','line_count','word_count','character_count','uploaded_at']