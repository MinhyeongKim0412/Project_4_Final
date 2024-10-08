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
        related_name='customuser_set',
        blank=True,
        help_text='사용자가 속한 그룹입니다. 사용자는 각 그룹에서 부여된 모든 권한을 얻습니다.',
        verbose_name='그룹'
    )

    # user_permissions 필드 수정
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='이 사용자에 대한 특정 권한입니다.',
        verbose_name='사용자 권한'
    )

    def __str__(self):
        return self.username  # 사용자 이름을 문자열로 반환


# 게시판 모델 (글 작성, 수정, 삭제, 조회 기능)
class Post(models.Model):
    TOPIC_CHOICES = [
        ('사는 얘기', '사는 얘기'),
        ('자랑하기', '자랑하기'),
        ('친목', '친목'),
        ('알립니다', '알립니다'),
    ]

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # 작성자 연결
    title = models.CharField(max_length=100)  # 제목
    content = models.TextField()  # 내용
    topic = models.CharField(max_length=10, choices=TOPIC_CHOICES, default='사는 얘기')
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

# 좋아요 모델
class Like(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # 좋아요를 누른 사용자
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes_list', null=True, blank=True)  # 게시글에 대한 좋아요
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes_list', null=True, blank=True)  # 댓글에 대한 좋아요
    created_at = models.DateTimeField(auto_now_add=True)  # 좋아요 생성일

    class Meta:
        unique_together = ('user', 'post', 'comment')  # 사용자, 게시글, 댓글 조합의 유일성 보장

    def __str__(self):
        return f'Like by {self.user} on {self.post or self.comment}'


# 싫어요 모델
class Dislike(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)  # 싫어요를 누른 사용자
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='dislikes_list', null=True, blank=True)  # 게시글에 대한 싫어요
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='dislikes_list', null=True, blank=True)  # 댓글에 대한 싫어요
    created_at = models.DateTimeField(auto_now_add=True)  # 싫어요 생성일

    class Meta:
        unique_together = ('user', 'post', 'comment')  # 사용자, 게시글, 댓글 조합의 유일성 보장

    def __str__(self):
        return f'Dislike by {self.user} on {self.post or self.comment}'
