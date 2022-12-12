from django.urls import path

from .views import SongListView, SongDetailView

urlpatterns = [
    path('', SongListView.as_view(), name='Songs_list'),
    path('<int:pk>/', SongDetailView.as_view(), name='Songs_detail'),
]