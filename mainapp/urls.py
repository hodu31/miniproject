from django.urls import path

### firstapp 폴더 하위에 있는 views.py 파일 읽어 들이기
# - 라이브러리 읽어들이는 것과 동일
from . import views

### 사용자가 요청할 수 있는 URL을 정의합니다.
# - url 하나당, views의 함수 한개를 호출할 수 있도록 매핑합니다.
# - url을 정의한다고 해서, 패턴(pattern)정의라고 합니다.
urlpatterns = [
    # - https://127.0.0.1:8000/login_chk/
    path('login_chk/', views.login_chk),
    # - https://127.0.0.1:8000/logout_chk/
    path('logout_chk/', views.logout_chk),
    # - https://127.0.0.1:8000/
    path('', views.index),
    # - https://127.0.0.1:8000/register/
    path('register/', views.Register),
    # - https://127.0.0.1:8000/register1/
    path('register1/', views.Register1),
    path('sign_in/', views.sign),
    # - https://127.0.0.1:8000//
    path('data_info/', views.Data_info),
    # - https://127.0.0.1:8000//
    path('recom/', views.Recom),
    # - https://127.0.0.1:8000//
    path('recom_dis/', views.Recom_dis),
    # - https://127.0.0.1:8000//
    path('dis_add/', views.dis_add),
    # - https://127.0.0.1:8000//
    path('insert_view/', views.Insert_view),
    # - https://127.0.0.1:8000//
    path('insert_view2/', views.Insert_view2),
    # - https://127.0.0.1:8000//
    path('prodprod/', views.prodprod),
    # - https://127.0.0.1:8000//
    path('naver/', views.naver),
    # - https://127.0.0.1:8000//
    path('statistic/', views.Statistic),
]