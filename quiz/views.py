from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question
from .serializers import QuestionSerializer
import pickle

# Create your views here.


class RandomQuestion(APIView):
    def get(self, request):
        question = Question.objects.filter().order_by("?")[0]
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
