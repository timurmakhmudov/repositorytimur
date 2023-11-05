from django.urls import path
from .views import index, top_sellers, advertisement_post, advertisements_detail

urlpatterns = [
    path('', index,name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('adv-post/', advertisement_post, name='adv-post'),
    path('advertisement/<int:pk>', advertisements_detail, name='adv-detail'),
]
