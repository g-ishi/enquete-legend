from django import forms


class MemberFields(forms.Field):
    """
    部員フォームの入力バリデーション
    """
    def clean(self, value):
        print('test')
        if '@' in value:
            raise forms.ValidationError('@は使用禁止！！')
        return value


class MemberForms(forms.Form):
    """
    部員作成画面で使用するフォームクラス
    """
    member_name = MemberFields(
        label='部員名',
        required=True,
    )
    
    def clean_member_name(self):
        """
        なぜかうまくいかない。
        あとで参考書見る。
        """
        member_name = self.cleaned_data['member_name']
        if '@' in member_name:
            raise forms.ValidationError('@ is not allowed!!')
        return member_name
