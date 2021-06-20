from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # <int:pk>
    # 整数値を期待：値がpkという名前でviewに渡される
    # 最後に '/' が必要
    path("post/<int:pk>/", views.post_detail, name="post_detail")
]
