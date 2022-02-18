from django.urls import path
from . import views
app_name='polls'


urlpatterns=[
    path('',views.index1,name='index1'),
    path('<int:pk>/',views.detail,name='detail'),
    path('<int:pk>/result/',views.result,name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('specifics/<int:question_id>/',views.detail,name='detail')

]