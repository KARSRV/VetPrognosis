from django.urls import path
from .views import chat_view,home,symptom_check,placeholder_view,upload_image,symptom_check_cow

urlpatterns = [
    path('', home, name='home'),
    path('cow/', symptom_check_cow, name='symptom_check_cow'),
    path('/Anon', chat_view, name='chat'),
    path('symp/', symptom_check, name='symptom_check'),  # Symptom checker view
    path('upload/', upload_image, name='upload_image'),
    path('api/placeholder/<int:param1>/<int:param2>/',placeholder_view, name='placeholder_view'),  # Placeholder API example
    
]