from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    # 艦娘
    path('kanmusu/', views.kanmusu_list, name='kanmusu_list'),   # 一覧
    path('kanmusu/add/', views.kanmusu_edit, name='kanmusu_add'),  # 登録
    path('kanmusu/mod/<int:kanmusu_id>/', views.kanmusu_edit, name='kanmusu_mod'),  # 修正
    path('kanmusu/del/<int:kanmusu_id>/', views.kanmusu_del, name='kanmusu_del'),   # 削除

    # 感想
    path('impression/<int:kanmusu_id>/', views.ImpressionList.as_view(), name='impression_list'),  # 一覧
    path('impression/add/<int:kanmusu_id>/', views.impression_edit, name='impression_add'),        # 登録
    path('impression/mod/<int:kanmusu_id>/<int:impression_id>/', views.impression_edit, name='impression_mod'),  # 修正
    path('impression/del/<int:kanmusu_id>/<int:impression_id>/', views.impression_del, name='impression_del'),   # 削除
]
