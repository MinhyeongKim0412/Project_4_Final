from django.shortcuts import render

def main(request):
    return render(request, 'main.html')

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')

def mypage_view(request):
    return render(request, 'mypage.html')

def delete_account_view(request):
    return render(request, 'delete_account.html')

def find_account_view(request):
    return render(request, 'find_account.html')

def board_view(request):
    return render(request, 'board.html')

def post_create_view(request):
    return render(request, 'post_create.html')

def post_edit_view(request, post_id):
    return render(request, 'post_edit.html')

def post_view(request, post_id):
    return render(request, 'post_view.html')

def post_reaction_view(request, post_id):
    return render(request, 'post_reaction.html')

def update_profile_view(request):
    return render(request, 'update_profile.html')