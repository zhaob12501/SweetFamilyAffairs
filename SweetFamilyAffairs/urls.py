from django.urls import path, include, re_path
from users.views import WeChatLoginView

urlpatterns = [
    path('login/', WeChatLoginView.as_view()),
    path('', include('items.urls')),
]
