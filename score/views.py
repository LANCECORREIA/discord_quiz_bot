from django import views
from django.shortcuts import render
from .serializers import ScoreSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import status
from .models import Score

# Create your views here.


class UpdateScores(APIView):
    def post(self, request):
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data["name"]
            points = serializer.validated_data["points"]
            if Score.objects.filter(name=name).exists():
                serializer = Score.objects.get(name=name)
                serializer.points += points
            serializer.save()
            return Response(None, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Leaderboard(ListAPIView):
    serializer_class = ScoreSerializer
    queryset = Score.objects.all()

    def get_queryset(self):
        return self.queryset.order_by("-points")[:10]
