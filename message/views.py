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
        self.friend_model = models.FriendModel

    def get(self, request, *args, **kwargs):
        # ページング
        page = kwargs.get('page', 1)

        message_list = self.message_model.objects.all()
        message_page = Paginator(message_list, 3)

        friend_list = self.friend_model.objects.all()
        for friend in friend_list:
            print(friend)

        context_data = {
            'message_forms': forms.MessageForm(),
            'message_list': message_page.get_page(page),
            'friend_list': friend_list,
        }
        return render(request, 'message_list.html', context_data)

    def post(self, request, *args, **kwargs):
        # 投稿の作成
        obj = models.MessageModel()
        message_form = forms.MessageForm(request.POST, instance=obj)
        message_form.save()

        message_list = self.message_model.objects.all()
        message_page = Paginator(message_list, 3)

        friend_list = self.friend_model.objects.all()

        context_data = {
            'message_forms': forms.MessageForm(),
            'message_list': message_page.get_page(1),
            'friend_list': friend_list,

        }
        return render(request, 'message_list.html', context_data)


class FormTest(View):
    """
    いろんな種類のformの動作確認用のクラス
    """

    def get(self, request, *args, **kwargs):
        context_data = {
            'goto': 'message:form_test',
            'forms': forms.TestForm(),
        }
        return render(request, 'form_test.html', context_data)

    def post(self, request, *args, **kwargs):
        text_data = request.POST.get('text_input', None)
        print(request.POST)
        context_data = {
            'goto': 'message:form_test',
            'text_data': text_data,
            'forms': forms.TestForm(request.POST),
        }
        return render(request, 'form_test.html', context_data)
