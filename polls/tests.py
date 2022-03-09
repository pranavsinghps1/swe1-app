#For unit Cases
from django.test import TestCase
import datetime
from django.urls import reverse

# from django.test import TestCase
from django.utils import timezone

from .models import Question


def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)