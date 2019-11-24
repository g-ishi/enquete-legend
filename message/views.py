from django.shortcuts import render
from django.views.generic import View
from django.core.paginator import Paginator

from . import models
from . import forms


class MessageList(View):
    """
    投稿一覧画面を表示するクラス
    """

    def __init__(self):
        self.message_model = models.MessageModel

    def get(self, request, *args, **kwargs):
        # ページング
        page = kwargs.get('page', 1)

        message_list = self.message_model.objects.all()
        message_page = Paginator(message_list, 3)
        context_data = {
            'message_forms': forms.MessageForm(),
            'message_list': message_page.get_page(page),
        }
        return render(request, 'message_list.html', context_data)

    def post(self, request, *args, **kwargs):
        # 投稿の作成
        obj = models.MessageModel()
        message_form = forms.MessageForm(request.POST, instance=obj)
        message_form.save()

        message_list = self.message_model.objects.all()
        message_page = Paginator(message_list, 3)
        context_data = {
            'message_forms': forms.MessageForm(),
            'message_list': message_page.get_page(1)
        }
        return render(request, 'message_list.html', context_data)
