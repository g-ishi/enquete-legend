from django import forms

from .models import MessageModel


class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageModel
        fields = ['title', 'content', 'friend']


class TestForm(forms.Form):
    """
    いろんな種類のフォームを試すためのフォームクラス
    """
    text = forms.CharField(
        label='name',
        required=False,
        max_length=10,
        min_length=5)
    mail = forms.EmailField(
        label='email',
        required=False,
        max_length=10,
        min_length=5
    )
    number_int = forms.IntegerField(
        required=False,
        label='int数字',
        help_text='数字を入力してください',
        max_value=100,
        min_value=5
    )
    float_num = forms.FloatField(
        required=False,
        max_value=10,
    )
    url_text = forms.URLField(
        required=False,
        label='URL入力',
        max_length=10,
        min_length=5,
    )
    # DateFieldのtype="date"にする方法
    # 参考) https://qiita.com/felyce/items/726496b9cecdaf05b6b1
    date_text = forms.DateField(
        required=False,
        label='日付',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    # TimeFieldのtype="time"にするのも上記と同じ方法でできる
    time_text = forms.TimeField(
        required=False,
        label='時間',
        widget=forms.TimeInput(attrs={'type': 'time'})
    )
    check_box_1 = forms.BooleanField(
        label='check 1',
        required=False,
    )
    check_box_2 = forms.BooleanField(
        label='check 2',
        required=False,
    )
    null_bool = forms.NullBooleanField(
        label='3択',
        required=False,
    )
