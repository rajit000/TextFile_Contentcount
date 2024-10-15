from django.db import models

class TextFileUpload(models.Model):
    filename = models.CharField(max_length=255)
    line_count = models.IntegerField()
    word_count = models.IntegerField()
    character_count = models.IntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.filename
