from django.db import models


# 部員マスタ
class MemberModel(models.Model):
    member_id = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=100)
    registration_date = models.DateField(auto_now_add=True)
    delete_flag = models.BooleanField(default=False)


# アンケートマスタ
class EnqueteModel(models.Model):
    enquete_id = models.AutoField(primary_key=True)
    enquete_name = models.CharField(max_length=200)
    member_id = models.ForeignKey(MemberModel, on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now_add=True)
    answer_date = models.DateField(null=True)
    delete_flag = models.BooleanField(default=False)


# アンケート回答種別マスタ
class ItemTypeModel(models.Model):
    item_type_id = models.AutoField(primary_key=True)
    item_type_name = models.CharField(max_length=200)
    registration_date = models.DateField(auto_now_add=True)
    delete_flag = models.BooleanField(default=False)


# アンケート項目マスタ
class ItemModel(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=200)
    item_type_id = models.ForeignKey(ItemTypeModel, on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now_add=True)
    delete_flag = models.BooleanField(default=False)


# アンケート回答結果
class AnswerModel(models.Model):
    answer_id = models.AutoField(primary_key=True)
    enquete_id = models.ForeignKey(EnqueteModel, on_delete=models.CASCADE)
    item_id = models.ForeignKey(ItemModel, on_delete=models.CASCADE)
    member_id = models.ForeignKey(MemberModel, on_delete=models.CASCADE)
    answer_content = models.CharField(max_length=200)
    registration_date = models.DateField(auto_now_add=True)
