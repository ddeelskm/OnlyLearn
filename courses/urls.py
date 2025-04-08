from django.urls import path

from courses import views

urlpatterns = [
    path('', views.CoursesView.as_view(), name='courses'),
    path('addcourses/', views.AddCourses.as_view(), name='addcourses'),
    path('addauthors/', views.AddAuthors.as_view(), name='addauthors'),
    path('addcategory/', views.AddCategory.as_view(), name='addcategory'),
    path('author/<slug:author_slug>/', views.AuthorDetail.as_view(), name='author_detail'),
    path('<slug:detail_slug>/', views.CoursesDetail.as_view(), name='courses_detail'),
]
