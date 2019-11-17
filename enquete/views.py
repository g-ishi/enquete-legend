from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from . import models
from . import forms

class enqueteList(View):
    """
    アンケート一覧画面を表示するクラス
    """
    def __init__(self):
        # 使用するmodelクラス
        self.member_model = models.MemberModel
        self.enquete_model = models.EnqueteModel

    def get(self, request, *args, **kwargs):
        member_list = self.member_model.objects.all()
        enquete_list = self.enquete_model.objects.all()
        context_data = {
            'test': 'test',
            'enquete_list': enquete_list,
            'member_list': member_list,
        }
        return render(request, 'enquete_list.html', context_data)

class enqueteCreate(View):
    """
    アンケート作成画面を表示するクラス
    """
    def __init__(self):
        pass

    def get(self, request, *args, **kwargs):
        member_forms = forms.MemberForms(request.GET or None)
        member_forms.is_valid()
        context_data = {
            'member_forms': member_forms
        }
        return render(request, 'member_create.html', context_data)

    def post(self, request, *args, **kwargs):
        member_name = request.POST.get('member_name', None)
        context_data = {
            'member_name': member_name
        }
        return render(request, 'member_create.html', context_data)
