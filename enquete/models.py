from django.db import models


# 部員マスタ
class MemberModel(models.Model):
    member_id = models.AutoField('部員ID', primary_key=True)
    member_name = models.CharField('部員名', max_length=100)
    registration_date = models.DateField('登録日', auto_now_add=True)
    delete_flag = models.BooleanField('削除フラグ', default=False)

    def __str__(self):
        return self.member_name


# アンケートマスタ
class EnqueteModel(models.Model):
    enquete_id = models.AutoField('アンケートID', primary_key=True)
    enquete_name = models.CharField('アンケート名', max_length=200)
    member_id = models.ForeignKey('MemberModel', on_delete=models.CASCADE)
    registration_date = models.DateField('登録日', auto_now_add=True)
    answer_date = models.DateField('回答日', null=True)
    delete_flag = models.BooleanField('削除フラグ', default=False)

    def __str__(self):
        return self.enquete_name
