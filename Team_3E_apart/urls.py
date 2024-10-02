from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.main, name='홈'),
    path('login/', views.login_view, name='로그인'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='로그인_연결'),
    path('logout/', views.custom_logout_view, name='로그아웃'),
    path('signup/', views.signup_view, name='회원가입'),
    path('mypage/', views.mypage_view, name='마이페이지'),
    path('update_profile/', views.update_profile_view, name='회원정보수정'),
    path('delete_account/', views.delete_account_view, name='회원탈퇴'),
    path('find_account/', views.find_account_view, name='정보찾기'),  # 아이디와 이메일 입력 페이지
    path('reset_password/<str:username>/', views.reset_password_view, name='비밀번호재설정'),  # 비밀번호 재설정 화면
    path('board/', views.board_view, name='게시판'),
    path('post/create/', views.post_create_view, name='글작성'),
    path('post/edit/<int:post_id>/', views.post_edit_view, name='글수정'),
    path('post/<int:post_id>/', views.post_view, name='글조회'),
]
