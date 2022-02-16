from django.urls import path
from . import views


urlpatterns=[
    path('',views.index1,name='index1'),
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/result/',views.result,name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('specifics/<int:question_id>/',views.detail,name='detail')


]