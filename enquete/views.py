from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator

from . import models
from . import forms


class MemberList(View):
    """
    部員一覧画面を表示するクラス
    """

    def __init__(self):
        # 使用するmodelクラス
        self.member_model = models.MemberModel

    def get(self, request, *args, **kwargs):
        member_list = self.member_model.objects.all()
        context_data = {
            'member_list': member_list,
        }
        return render(request, 'member_list.html', context_data)


class MemberCreate(View):
    """
    部員作成画面を表示するクラス
    """

    def __init__(self):
        pass

    def get(self, request, *args, **kwargs):
        member_forms = forms.MemberForms(request.GET or None)
        context_data = {
            'forms': member_forms,
        }
        return render(request, 'member_create.html', context_data)

    def post(self, request, *args, **kwargs):
        member_forms = forms.MemberForms(request.POST or None)
        # 入力フォームにエラーがある場合
        if member_forms.errors:
            context_data = {
                'forms': member_forms,
            }
            return render(request, 'member_create.html', context_data)

        # 入力フォームがOKなら登録して一覧画面へリダイレクト
        member_name = request.POST['member_name']
        member = models.MemberModel(member_name=member_name)
        member.save()
        return redirect(to='/enquete/list/')


class MemberDetail(View):
    """
    部員の詳細画面を表示するクラス
    """

    def __init__(self):
        self.member_model = models.MemberModel

    def get(self, request, *args, **kwargs):
        member_forms = forms.MemberForms(request.GET or None)
        key_id = ''
        # クエリパラメータはrequest.GETに入るが
        # urlsで指定した変数はkwargsに入ってくる。
        if 'member_id' in kwargs:
            key_id = kwargs['member_id']

        member = self.member_model.objects.get(member_id=key_id)
        context_data = {
            'member': member,
            'forms': member_forms,
        }
        return render(request, 'member_detail.html', context_data)


class MemberUpdate(View):
    """
    部員の更新画面を表示するクラス
    """

    def __init__(self):
        self.member_model = models.MemberModel

    def get(self, request, *args, **kwargs):
        key_id = ''
        if 'member_id' in kwargs:
            key_id = kwargs['member_id']

        member = self.member_model.objects.get(member_id=key_id)

        # フォームの初期値を設定
        initial_dict = {
            'member_name': member.member_name,
        }

        member_forms = forms.MemberForms(request.GET or None,
                                         initial=initial_dict)
        context_data = {
            'member': member,
            'forms': member_forms
        }
        return render(request, 'member_update.html', context_data)

    def post(self, request, *args, **kwargs):
        member_forms = forms.MemberForms(request.POST or None)
        # 入力フォームにエラーがある場合
        if member_forms.errors:
            context_data = {
                'forms': member_forms,
            }
            return render(request, 'member_update.html', context_data)

        # クエリストURLからmember_idを取得　更新の検索キーにする
        key_id = ''
        if 'member_id' in kwargs:
            key_id = kwargs['member_id']

        # 入力フォームがOKなら更新して一覧画面へリダイレクト
        member = self.member_model.objects.get(member_id=key_id)
        member.member_name = request.POST['member_name']
        member.save()
        return redirect(to='/enquete/list/')


class MemberDeleteConfirm(View):
    """
    部員削除確認画面を表示するクラス
    """

    def __init__(self):
        self.member_model = models.MemberModel

    def get(self, request, *args, **kwargs):
        key_id = ''
        # url変数はkwargsに入っている
        if 'member_id' in kwargs:
            key_id = kwargs['member_id']

        member = self.member_model.objects.get(member_id=key_id)
        context_data = {
            'member': member,
        }
        return render(request, 'member_delete_confirm.html', context_data)

    def post(self, request, *args, **kwargs):
        key_id = ''
        if 'member_id' in kwargs:
            key_id = kwargs['member_id']

        member = self.member_model.objects.get(member_id=key_id)
        member.delete_flag = True
        member.save()
        return redirect(to='/enquete/delete/result')


class MemberDeleteResult(View):
    """
    部員削除確認画面を表示するクラス
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'member_delete_result.html')


class MemberFind(View):
    """
    部員検索画面を表示するクラス
    """

    def __init__(self):
        self.member_model = models.MemberModel

    def get(self, request, *args, **kwargs):
        find_forms = forms.FindFroms(request.GET or None)
        context_data = {
            'forms': find_forms,
        }
        return render(request, 'member_find.html', context_data)

    def post(self, request, *args, **kwargs):
        find_forms = forms.FindFroms(request.POST or None)

        # 入力された検索キーで検索
        find_key = request.POST['find']
        # OR検索は以下のようにして行う
        # 検索結果のソートにはorder_byを使用する
        find_results = self.member_model.objects.filter(
            Q(member_name__contains=find_key) | Q(member_id__contains=find_key))\
            .order_by('member_name')

        context_data = {
            'find_results': find_results,
            'forms': find_forms,
        }
        return render(request, 'member_find.html', context_data)


class MemberSort(View):
    """
    ソート機能付きの部員一覧画面
    """

    def __init__(self):
        # 使用するmodelクラス
        self.member_model = models.MemberModel

    def get(self, request, *args, **kwargs):
        # 正規のソートキーが指定された場合に、ソートする
        # ソートキーが指定されてない場合は、defaultが入っているものとする
        sort_key = ''
        member_list = {}
        print(kwargs)
        if 'sort_key' in kwargs:
            sort_key = kwargs['sort_key']
            if sort_key != 'default':
                print(1)
                member_list = self.member_model.objects.all().order_by(sort_key)
            else:
                print(2)
                member_list = self.member_model.objects.all()

        context_data = {
            'member_list': member_list,
        }
        return render(request, 'member_sort.html', context_data)


class MemberPage(View):
    """
    ページング機能付きの一覧画面
    """

    def __init__(self):
        # 使用するmodelクラス
        self.member_model = models.MemberModel

    def get(self, request, *args, **kwargs):
        # ページングのUIは下記が参考になるかも
        # https://djangobrothers.com/blogs/django_pagination/
        member_list = self.member_model.objects.all()
        member_page = Paginator(member_list, 4)
        if 'page_num' in kwargs:
            page_num = kwargs.get('page_num', 1)
        print(request.GET)
        print(kwargs)
        context_data = {
            'member_list': member_page.get_page(page_num),
        }
        return render(request, 'member_page.html', context_data)
