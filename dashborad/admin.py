from django.contrib import admin

from .models import EnqueteModel
from .models import MemberModel
from .models import ItemModel
from .models import ItemTypeModel
from .models import AnswerModel


# 部員マスタ
class MemberAdmin(admin.ModelAdmin):
    list_display = ('member_id', 'member_name', 'registration_date', 'delete_flag')

# アンケートマスタ
class EnqueteAdmin(admin.ModelAdmin):
    list_display = ('enquete_id', 'enquete_name', 'member_id', 'registration_date',
                    'answer_date', 'delete_flag')


# アンケート項目マスタ
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'item_name', 'item_type_id', 'registration_date', 'delete_flag')


# アンケート項目種別マスタ
class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('item_type_id', 'item_type_name', 'registration_date', 'delete_flag')


# アンケート回答結果マスタ
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_id', 'enquete_id', 'item_id', 'member_id', 'answer_content', 'registration_date')


# Register your models here.
admin.site.register(EnqueteModel, EnqueteAdmin)
admin.site.register(MemberModel, MemberAdmin)
admin.site.register(ItemModel, ItemAdmin)
admin.site.register(ItemTypeModel, ItemTypeAdmin)
admin.site.register(AnswerModel, AnswerAdmin)
