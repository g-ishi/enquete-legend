from django.urls import path

from . import views

app_name = 'enquete'

urlpatterns = [
    path('list/', views.MemberList.as_view(), name='member_list'),
    path('create/', views.MemberCreate.as_view(), name='member_create'),
    path('detail/<member_id>/',
         views.MemberDetail.as_view(), name='member_detail'),
    path('update/<member_id>',
         views.MemberUpdate.as_view(), name='member_update'),
    path('delete/confirm/<member_id>',
         views.MemberDeleteConfirm.as_view(), name='member_delete_confrim'),
    path('delete/result/',
         views.MemberDeleteResult.as_view(), name='member_delete_result'),
    path('find/', views.MemberFind.as_view(), name='member_find'),
    path('sort/<sort_key>', views.MemberSort.as_view(), name='member_sort'),
    path('page/<int:page_num>', views.MemberPage.as_view(), name='member_page'),
]
