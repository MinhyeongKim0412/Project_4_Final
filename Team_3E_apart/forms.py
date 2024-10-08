from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Post, Comment  # CustomUser 및 Post 모델 import

class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=True)  # 전화번호 필드
    email = forms.EmailField(required=True)  # 이메일 필드
    apartment_number = forms.CharField(max_length=10, required=False)  # 아파트 번호 필드
    address = forms.CharField(max_length=255, required=True)  # 주소 필드
    detail_address = forms.CharField(max_length=255, required=False)  # 상세 주소 필드
    postcode = forms.CharField(max_length=10, required=False)  # 우편번호 필드

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'phone', 'email', 
                  'apartment_number', 'address', 'detail_address', 'postcode')  # 필요한 필드 포함

class PostForm(forms.ModelForm):
    TOPIC_CHOICES = [
        ('사는 얘기', '사는 얘기'),
        ('자랑하기', '자랑하기'),
        ('친목', '친목'),
        ('알립니다', '알립니다'),
    ]

    topic = forms.ChoiceField(choices=TOPIC_CHOICES, required=True)  # 토픽 필드
    title = forms.CharField(max_length=100, required=True)  # 제목 필드
    content = forms.CharField(widget=forms.Textarea, required=True)  # 내용 필드

    class Meta:
        model = Post
        fields = ('topic', 'title', 'content')  # 토픽, 제목, 내용 포함


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': '댓글을 입력하세요'})  # placeholder 속성 추가 (선택 사항)
        }
        labels = {
            'content': '',  # 'Content:' 레이블을 없앰
        }