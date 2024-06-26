from django.db import models

class ResearchPaper(models.Model):
    file = models.FileField(upload_to='research_papers/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    word_count = models.IntegerField(default=0)
    sentence_count = models.IntegerField(default=0)
    top_words = models.JSONField(default=dict)
    top_phrases = models.JSONField(default=dict)

    def __str__(self):
        return self.file.name