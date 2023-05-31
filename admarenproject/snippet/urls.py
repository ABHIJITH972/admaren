from django.urls import path
from .views import *

urlpatterns = [
    
    path('login/',Loginview.as_view(),name='Login'),
    path('overview/', OverView.as_view(), name='snippet_overview'),
    path('create/', Create.as_view(), name='snippet_create'),
    path('detail/<int:snippet_id>/', Detail.as_view(), name='snippet_detail'),
    path('update/<int:snippet_id>/', Update.as_view(), name='snippet_update'),
    path('delete/<int:snippet_id>/', Delete.as_view(), name='snippet_delete'),
    path('tags/', TagList.as_view(), name='tag_list'),
    path('tag/<int:tag_id>/', TagDetail.as_view(), name='tag_detail'),
    
]