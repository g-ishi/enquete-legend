from django import forms

import string


class MemberForms(forms.Form):
    """
    部員作成画面で使用するフォームクラス
    """
    member_name = forms.CharField(
        label='部員名',
        required=True,
        max_length=100
    )

    def clean_member_name(self):
        """
        カスタムバリデーションを行う関数
        clean_<フィールド名>で定義することで呼び出される
        """
        # 数字が使用されていないことを確認する
        member_name = self.cleaned_data['member_name']
        if 'admin' in member_name:
            raise forms.ValidationError('adminは名前に使用できません！')
        return member_name


class FindFroms(forms.Form):
    """
    検索ボックスとして使用するフォーム
    """
    find = forms.CharField(
        label='検索',
        required=False,
    )
