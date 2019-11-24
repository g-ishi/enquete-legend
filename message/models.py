from django.db import models


# 人物マスタ
class FriendModel(models.Model):
    name = models.CharField(max_length=100)
    mail = models.CharField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(default=0)
    birthday = models.DateField()

    def __str__(self):
        return self.name


class MessageModel(models.Model):
    friend = models.ForeignKey(FriendModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' posted by ' + self.friend.name

    class Meta:
        # デフォルトでのソート順を指定する
        ordering = ('pub_date',)
