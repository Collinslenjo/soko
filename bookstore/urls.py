from .views import *
from . import views
from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', ListBooks.as_view(), name='books'),
    url(r'^books/(?P<pk>[0-9]+)$', BookDetails.as_view()),
    url(r'^categories/$', ListCategories.as_view(), name='categories'),
    url(r'^categories/(?P<pk>[0-9]+)$', CategoryDetails.as_view()),
    url(r'^rentbooks/$', ListRentedBooks.as_view(), name='rentbooks'),
    url(r'^rentbooks/(?P<pk>[0-9]+)$', rentedBookDetails.as_view()),
    url(r'^auth/?$', obtain_auth_token)
]

urlpatterns = format_suffix_patterns(urlpatterns)