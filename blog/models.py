from django.db import models
from django.conf import settings
from django.utils import timezone

# Models.model でDjangoに「データベースに保存すべき」と伝える


class Post(models.Model):
    # 以下のフィールドは「なくてもよい」とは書かれていないので値が設定されることが期待される.
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
