from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

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
    path('mypage_posts/', views.my_posts_view, name='내게시물'),  # 내 게시물
    path('mypage_comments/', views.my_comments_view, name='내댓글'),  # 내 댓글
    path('mypage_liked_posts/', views.my_liked_posts_view, name='내좋아요누른게시물'),  # 내 좋아요 누른 게시물
    path('like/<int:post_id>/', views.like_post, name='좋아요'),  # 좋아요 추가
    path('unlike/<int:post_id>/', views.unlike_post, name='좋아요취소'),  # 좋아요 취소
    path('dislike/<int:post_id>/', views.dislike_post, name='싫어요'),  # 싫어요 추가
    path('undislike/<int:post_id>/', views.undislike_post, name='싫어요취소'),  # 싫어요 취소
    path('profile/', views.profile, name='프로필사진'),
    path('profile/upload/', views.upload_profile_picture, name='프로필사진업로드'),
    path('profile/delete/', views.delete_profile_picture, name='프로필사진삭제'),  # 프로필 사진 삭제 URL 추가
    path('calculator/', views.energy_calculator, name='요금계산기'),  # 전력요금계산기
    path('energy/usage/', views.energy_usage, name='에너지소비'),  # 실시간 에너지 소비량
    path('ranking/', views.energy_ranking, name='랭킹'),  # 에너지 절약 랭킹
    path('public-usage/', views.public_energy_usage, name='전기사용량'),  # 공용전기사용량 조회
    path('campaign/', views.campaign, name='캠페인'),  # 진행중인 캠페인
    path('facility/', views.facility_reservation, name='편의시설예약'),  # 편의시설 예약
    path('search/', views.search, name='검색'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
