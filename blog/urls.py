from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
	path('api/articles/', views.ArticleList.as_view(), name='article_list'),
	path('api/articles/<str:pk>/', views.ArticleDetail.as_view(), name='article_detail'),
	path('api/categories/', views.CategoryList.as_view(), name='category_list'),
]