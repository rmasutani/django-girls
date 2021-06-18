from django.contrib import admin
from .models import Post

# 作ったモデルをAdminページで見れるようにする
admin.site.register(Post)
