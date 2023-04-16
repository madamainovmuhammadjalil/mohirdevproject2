from django.urls import path
from .views import HomepageViews,AboutpageViews,Telpageviews

urlpatterns = [
    path('tel/',Telpageviews.as_view(),name = 'tel'),
    path('about/',AboutpageViews.as_view(),name = 'about'),
    path('',HomepageViews.as_view(),name = 'home'),
]