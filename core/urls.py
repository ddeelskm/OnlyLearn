from django.urls import path

from core import views
from core.views import page_not_found

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('contact/', views.contacts, name='contact'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('addbanner/', views.AddBanner.as_view(), name='add_banner'),
    path('addreviews/', views.AddReviews.as_view(), name='add_reviews'),
]


handler404 = page_not_found
