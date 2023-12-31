from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from habit_tracker.models import Habit
from habit_tracker.paginators import HabitPaginator
from habit_tracker.permissions import IsOwner
from habit_tracker.serializers import HabitSerializer


class HabitCreateAPIView(CreateAPIView):
    """Habit create"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]


class HabitListAPIView(ListAPIView):
    """Shows list of habits"""
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitRetrieveAPIView(RetrieveAPIView):
    """Get one habit on id"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitUpdateAPIView(UpdateAPIView):
    """update habit"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitDestroyAPIView(DestroyAPIView):
    """Destroys a habit"""
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class PublicHabitListAPIView(generics.ListAPIView):
    """List of public habits"""
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = [IsAuthenticated]





