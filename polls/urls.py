from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('',views.HomeView.as_view(),name = 'home'),
    path('detail/<pk>/',views.PollsDetailView.as_view(),name = 'question'),
    path('vote/',views.RegisterVoteView.as_view(),name = 'vote'),
    path('comment/',views.SaveCommentView.as_view(),name = 'comment'),
]