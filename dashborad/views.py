from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse

from .models import EnqueteModel
from .models import MemberModel
from .models import AnswerModel


# Create your views here.
class Test(TemplateView):
    template_name = 'hello.html'


class Enquetedashborad(ListView):
    template_name = 'dashborad.html'
    model = EnqueteModel
    paginate_by = 5


class EnqueteDetail(DetailView):
    template_name = 'detail.html'
    model = EnqueteModel

# アンケート回答
class EnqueteAnswer(CreateView):
    template_name = 'answer.html'
    model = AnswerModel
    fields = ('answer_id', 'enquete_id', 'item_id', 'member_id', 'answer_content')
    success_url = reverse_lazy('dashborad')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # アンケートに対応する項目を表示するため
        context['answer_object_list'] = AnswerModel.objects.filter(enquete_id=self.kwargs.get('pk'))
        return context


# class EnqueteCreate(CreateView):
#     # TODO:質問項目を選択してアンケートを作成できるようにする
#     # TODO:複数モデルにまたがる処理は、Templateとかでやるかも
#     # TODO:form.pyでの処理がわかったら更新する
#     template_name = 'create.html'
#     model = EnqueteModel
#     fields = ('member_id', 'enquete_name', 'answer_date')
#     success_url = reverse_lazy('dashborad')

class EnqueteCreate(TemplateView):
    # TODO:質問項目を選択してアンケートを作成できるようにする
    # TODO:複数モデルにまたがる処理は、Templateとかでやるかも
    # TODO:form.pyでの処理がわかったら更新する
    template_name = 'create.html'
    model = EnqueteModel
    fields = ('member_id', 'enquete_name', 'answer_date')
    success_url = reverse_lazy('dashborad')



class EnqueteDelete(DeleteView):
    # TODO:削除フラグを更新する処理に変更する
    # TODO:deleteviewではなくupdateviewで実装する
    template_name = 'delete.html'
    model = EnqueteModel
    success_url = reverse_lazy('dashborad')


# TODO:アンケート回答画面を作成する

