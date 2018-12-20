from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('<int:pk>/results/',views.ResultsView.as_view(),name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote'),

    # url(r'^$',views.index, name='index'),
    #     # url(r'^(?P<question_id>[0-9]+)/$',views.detail,name='detail'),
    #     # url(r'^(?P<question_id>[0-9]+)/results/$',views.results,name='results'),
    #     # url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
]