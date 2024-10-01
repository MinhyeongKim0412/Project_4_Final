from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='홈'),  # 루트 URL에서 main 뷰 처리
    path('login/', views.login_view, name='로그인'),
    path('signup/', views.signup_view, name='회원가입'),
    path('mypage/', views.mypage_view, name='마이페이지'),
    path('update_profile/', views.update_profile_view, name='회원정보수정'),
    path('delete_account/', views.delete_account_view, name='회원탈퇴'),
    path('find_account/', views.find_account_view, name='정보찾기'),
    path('board/', views.board_view, name='게시판'),
    path('post/create/', views.post_create_view, name='글작성'),
    path('post/edit/<int:post_id>/', views.post_edit_view, name='글수정'),
    path('post/<int:post_id>/', views.post_view, name='글조회'),
]
