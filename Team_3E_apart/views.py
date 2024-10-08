from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required  # 로그인 필요 데코레이터 추가
from .forms import CustomUserCreationForm, PostForm, CommentForm  # 커스텀 사용자 생성 폼 및 게시글 작성을 위한 폼 import
from .models import CustomUser, Post, Comment, Like, Dislike  # Post 모델 import

def main(request):
    return render(request, 'main.html', {'user': request.user})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # 사용자 인증
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # 자동 로그인
            messages.success(request, f"{username}님 안녕하세요, 반갑습니다!")  # 로그인 성공 메시지
            return redirect('홈')  # 로그인 후 홈으로 리다이렉트 (적절한 URL 이름으로 변경)
        else:
            messages.error(request, "아이디 또는 비밀번호가 잘못되었습니다.")  # 로그인 실패 시 오류 메시지
    
    return render(request, 'login.html')  # GET 요청 시 로그인 페이지 반환

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # 커스텀 폼 인스턴스 생성
        if form.is_valid():
            user = form.save()  # 사용자 저장
            login(request, user)  # 자동 로그인
            messages.success(request, "회원가입이 완료되었습니다.")  # 회원가입 성공 메시지
            return redirect('홈')  # 가입 후 홈으로 리다이렉트
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'signup.html', {'form': form})  # 폼 전달

# 마이페이지
def mypage_view(request):
    if request.user.is_authenticated:
        user = request.user  # 현재 로그인한 사용자
        post_count = Post.objects.filter(author=user).count()  # 사용자가 작성한 게시물 수
        comment_count = Comment.objects.filter(author=user).count()  # 사용자가 작성한 댓글 수

        context = {
            'user': user,
            'post_count': post_count,
            'comment_count': comment_count,
            # 필요한 다른 컨텍스트 데이터 추가
        }
        return render(request, 'mypage.html', context)  # 템플릿 이름은 상황에 맞게 수정하세요.
    else:
        return redirect('로그인')  # 로그인 페이지로 리다이렉트


def custom_logout_view(request):
    logout(request)  # 사용자를 로그아웃합니다.
    messages.success(request, '로그아웃되었습니다!')  # 성공 메시지를 추가합니다.
    return redirect('홈')  # 홈 화면으로 리다이렉트합니다.

def delete_account_view(request):
    if request.method == 'POST':
        request.user.delete()  # 사용자 삭제
        logout(request)  # 로그아웃
        messages.success(request, "로그아웃이 완료되었습니다.")  # 로그아웃 성공 메시지
        return redirect('main')  # 메인 페이지로 리다이렉트
    return render(request, 'delete_account.html')

# 비밀번호 재설정 요청 뷰
def find_account_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        try:
            # 커스텀 사용자 모델을 사용하여 사용자 찾기
            user = CustomUser.objects.get(username=username, email=email)
            return redirect('비밀번호재설정', username=user.username)  # 비밀번호 재설정 화면으로 이동
        except CustomUser.DoesNotExist:
            messages.error(request, '해당 아이디와 이메일이 일치하는 사용자를 찾을 수 없습니다.')
            return redirect('정보찾기')  # 다시 정보 찾기 페이지로 이동
    return render(request, 'find_account.html')

# 비밀번호 재설정 화면 뷰
def reset_password_view(request, username):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password == confirm_password:
            user = User.objects.get(username=username)
            user.set_password(new_password)
            user.save()
            messages.success(request, '비밀번호가 성공적으로 재설정되었습니다.')
            return redirect('로그인')  # 로그인 페이지로 이동
        else:
            messages.error(request, '비밀번호가 일치하지 않습니다.')

    return render(request, 'reset_password.html', {'username': username})

def board_view(request):
    posts = Post.objects.all()  # 모든 게시글 가져오기
    return render(request, 'board.html', {'posts': posts})

@login_required  # 로그인한 사용자만 접근 가능
def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Post 객체 생성
            post.author = request.user  # 현재 사용자 지정
            post.save()  # 데이터베이스에 저장
            messages.success(request, '게시글이 성공적으로 작성되었습니다.')  # 작성 성공 메시지
            return redirect('게시판')  # 게시판으로 리다이렉트
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})

@login_required  # 로그인한 사용자만 접근 가능
def post_edit_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # 게시글 가져오기
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)  # 기존 게시글 인스턴스를 사용하여 폼 생성
        if form.is_valid():
            form.save()  # 수정사항 저장
            messages.success(request, '게시글이 성공적으로 수정되었습니다.')  # 수정 성공 메시지
            return redirect('글조회', post_id=post.id)  # 수정 후 게시글 보기로 리다이렉트
    else:
        form = PostForm(instance=post)  # GET 요청 시 기존 게시글 데이터로 폼 생성
    return render(request, 'post_edit.html', {'form': form, 'post': post})  # 수정 폼과 게시글 데이터 전달

def post_view(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comments.all()  # 해당 게시물의 모든 댓글 가져오기

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user  # 현재 사용자 설정
            comment.save()
            return redirect('글조회', post_id=post.id)  # 새로 고침

    else:
        form = CommentForm()

    return render(request, 'post_view.html', {'post': post, 'comments': comments, 'form': form})

def post_reaction_view(request, post_id):
    return render(request, 'post_reaction.html')

@login_required  # 로그인한 사용자만 접근 가능
def update_profile_view(request):
    if request.method == 'POST':
        # 사용자 정보 수정
        username = request.POST.get('username')
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')

        # 사용자 정보 업데이트
        request.user.username = username
        request.user.email = email
        
        if new_password:
            request.user.set_password(new_password)  # 새 비밀번호 설정
        
        request.user.save()  # 변경사항 저장
        messages.success(request, '회원정보가 성공적으로 수정되었습니다.')  # 성공 메시지
        return redirect('마이페이지')  # 수정 후 마이페이지로 리다이렉트
    return render(request, 'update_profile.html')  # GET 요청 시 수정 폼 반환

# 내 게시물 뷰
@login_required  # 로그인한 사용자만 접근 가능
def my_posts_view(request):
    # 현재 사용자의 게시물 가져오기
    posts = Post.objects.filter(author=request.user)  # 현재 사용자에 의해 작성된 게시물
    post_count = posts.count()  # 게시물 수
    # 현재 사용자가 작성한 댓글 수 가져오기
    comment_count = Comment.objects.filter(author=request.user).count()  # 현재 사용자에 의해 작성된 댓글 수
    return render(request, 'mypage_posts.html', {
        'posts': posts,
        'post_count': post_count,
        'comment_count': comment_count  # 댓글 수 전달
    })  # 게시물 템플릿 렌더링

# 내 댓글 뷰
@login_required  # 로그인한 사용자만 접근 가능
def my_comments_view(request):
    # 현재 사용자가 작성한 댓글 가져오기
    comments = Comment.objects.filter(author=request.user)  # 현재 사용자에 의해 작성된 댓글
    comment_count = comments.count()  # 댓글 수
    # 현재 사용자가 작성한 게시물 수 가져오기
    post_count = Post.objects.filter(author=request.user).count()  # 현재 사용자에 의해 작성된 게시물 수
    return render(request, 'mypage_comments.html', {
        'comments': comments,
        'comment_count': comment_count,  # 댓글 수 전달
        'post_count': post_count  # 게시물 수 전달
    })  # 댓글 템플릿 렌더링

# 내 좋아요 누른 게시물 뷰
@login_required  # 로그인한 사용자만 접근 가능
def my_liked_posts_view(request):
    # 현재 사용자가 좋아요 누른 게시물 가져오기
    liked_posts = Post.objects.filter(like__user=request.user)  # 현재 사용자가 좋아요 누른 게시물
    return render(request, 'mypage_liked_posts.html', {'liked_posts': liked_posts})  # 좋아요 누른 게시물 템플릿 렌더링

# 게시물에 좋아요 추가
@require_POST
@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # 좋아요 모델 인스턴스 생성
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        # 이미 좋아요를 눌렀다면 아무 것도 하지 않음
        return JsonResponse({'status': 'already_liked'}, status=200)
    
    # 좋아요 수 증가
    post.likes += 1
    post.save()
    return JsonResponse({'status': 'liked', 'likes': post.likes})

# 게시물에서 좋아요 취소
@require_http_methods(["DELETE"])
@login_required
def unlike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    try:
        # 좋아요 모델 인스턴스 삭제
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        # 좋아요 수 감소
        post.likes -= 1
        post.save()
        return JsonResponse({'status': 'unliked', 'likes': post.likes})
    except Like.DoesNotExist:
        return JsonResponse({'status': 'not_liked'}, status=404)

# 게시물에 싫어요 추가
@require_POST
@login_required
def dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    # 싫어요 모델 인스턴스 생성
    dislike, created = Dislike.objects.get_or_create(user=request.user, post=post)
    if not created:
        # 이미 싫어요를 눌렀다면 아무 것도 하지 않음
        return JsonResponse({'status': 'already_disliked'}, status=200)

    # 싫어요 수 증가
    post.dislikes += 1
    post.save()
    return JsonResponse({'status': 'disliked', 'dislikes': post.dislikes})

# 게시물에서 싫어요 취소
@require_http_methods(["DELETE"])
@login_required
def undislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    try:
        # 싫어요 모델 인스턴스 삭제
        dislike = Dislike.objects.get(user=request.user, post=post)
        dislike.delete()
        # 싫어요 수 감소
        post.dislikes -= 1
        post.save()
        return JsonResponse({'status': 'undisliked', 'dislikes': post.dislikes})
    except Dislike.DoesNotExist:
        return JsonResponse({'status': 'not_disliked'}, status=404)
