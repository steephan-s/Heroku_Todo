from django.db import models
from datetime import datetime
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Task(models.Model):
    todo_text = models.CharField(max_length=200)
    add_date = models.DateTimeField(default=datetime.now, blank=True)
    completed = models.BooleanField(default=False)