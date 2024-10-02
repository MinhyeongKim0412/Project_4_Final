from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth import get_user_model

# 사용자 모델 커스터마이징 (로그인, 회원가입, 회원 정보 관리 등)
class CustomUser(AbstractUser):
    apartment_number = models.CharField(max_length=10, blank=True, null=True)  # 아파트 번호 추가
    phone = models.CharField(max_length=15, blank=False, default='000-0000-0000')  # 전화번호 필드에 기본값 추가
    email = models.EmailField(unique=True, blank=False)  # 이메일 필드 추가
    address = models.CharField(max_length=255, blank=False, default='Unknown address')
    detail_address = models.CharField(max_length=255, blank=True)  # 상세 주소 필드 추가
    postcode = models.CharField(max_length=10, blank=True)  # 우편번호 필드 추가

    # groups 필드 수정
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # 커스텀 유저 모델에 대한 고유한 이름
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions '
                  'granted to each of their groups.',
        verbose_name='groups'
    )

    # user_permissions 필드 수정
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # 커스텀 유저 모델에 대한 고유한 이름
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username  # 사용자 이름을 문자열로 반환

# 게시판 모델 (글 작성, 수정, 삭제, 조회 기능)
class Post(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # 작성자 연결
    title = models.CharField(max_length=100)  # 제목
    content = models.TextField()  # 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일
    updated_at = models.DateTimeField(auto_now=True)  # 수정일
    likes = models.IntegerField(default=0)  # 좋아요 수
    dislikes = models.IntegerField(default=0)  # 싫어요 수

    def __str__(self):
        return self.title  # 제목을 문자열로 반환

# 댓글 모델 (게시글에 대한 댓글 기능)
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # 게시글과 연결
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # 작성자 연결
    content = models.TextField()  # 댓글 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일
    updated_at = models.DateTimeField(auto_now=True)  # 수정일

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'  # 댓글 작성자와 게시글을 문자열로 반환
