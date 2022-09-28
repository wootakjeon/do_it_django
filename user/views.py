import bcrypt
import jwt
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
import user
from do_it_django_prj.settings import SECRET_KEY
from .models import User
from .models import Post
from .models import Comment
from .forms import BoardWriteForm
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator
from django import template
import MySQLdb

register = template.Library()


# Create your views here.


def index(request):
    return render(request, 'user/index.html')


def login(request):
    if request.method == 'POST':
        if User.objects.filter(email=request.POST['email']).exists():
            user = User.objects.get(email=request.POST['email'])
            user_password = user.password.encode('utf=8')

            if bcrypt.checkpw(request.POST['password'].encode('utf=8'), user_password):
                token = jwt.encode({"id": user.email}, SECRET_KEY, algorithm="HS256")
                request.session['user'] = user.email
                return redirect("index")
            return render(request, "user/login.html")
    else:
        return render(request, "user/login.html")

def join(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['passwordCheck']:
            password_not_hashed = request.POST['password']
            hashed_password = bcrypt.hashpw(password_not_hashed.encode('utf=8'), bcrypt.gensalt())
            User(
                email=request.POST['email'],
                password=hashed_password.decode('utf=8'),
                name=request.POST['name'],
                nickname=request.POST['nickname'],
                tel=request.POST['tel'],
                role=request.POST['gender']
            ).save()
            return redirect('login')
        return render(request, 'user/join_select.html')
    else:
        form = UserCreationForm
        return render(request, 'user/join_select.html', {'form': form})

def join_select(request):
    return render(request, 'user/join_select.html')

def join_mentor(request):
    return render(request, 'user/join_mentor.html')

def join_mentee(request):
    return render(request, 'user/join_mentee.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def community(request):
    return render(request,'user/community.html')

def new_writing(request):
    login_session = request.session.get('login_session', '')
    context = {'login_session': login_session}

    if request.method == 'GET':
        write_form = BoardWriteForm()
        context['forms'] = write_form
        return render(request, 'user/new_writing.html', context)

    elif request.method == 'POST':
        write_form = BoardWriteForm(request.POST)

        if write_form.is_valid():

            post = Post(
                title=write_form.title,
                text=write_form.text,
                author_id=request.session['user'],
                show_ct=0

            )
            post.save()
            return redirect('/community')
        else:
            context['forms'] = write_form
            if write_form.errors:
                for value in write_form.errors.values():
                    context['error'] = value
            return render(request, 'user/new_writing.html', context)



    # return render(request,'user/new_writing.html')

def community_post(request):
    return render(request,'user/community_post.html')

def mypost(request):
    return render(request,'user/mypost.html')

def board(request):
    boards = Post.objects.all().select_related('author').order_by('-id')
    boards_count = len(boards)
    page = request.GET.get('page', 1)
    paginator = Paginator(boards, 5)
    board_list = paginator.get_page(page)
    return render(request, 'user/board.html',
                  {'boards': boards, 'board_list': board_list, 'boards_count': boards_count, 'page': page})


def board_write(request):
     login_session = request.session.get('login_session', '')
     context = {'login_session': login_session}

     if request.method == 'GET':
         write_form = BoardWriteForm()
         context['forms'] = write_form
         return render(request,'user/new_writing.html')

     elif request.method == 'POST':
         write_form = BoardWriteForm(request.POST)

         if write_form.is_valid():
             post = Post(
                 title=write_form.title,
                 text=write_form.text,
                 author_id=request.session['user'],
                 show_ct=0
             )
             post.save()
             return redirect('/new_writing')
         else:
             context['forms'] = write_form
             if write_form.errors:
                 for value in write_form.errors.values():
                     context['error'] = value
             return render(request,'user/new_writing.html')

def cover_letter(request):
    return render(request,'user/cover_letter.html')

def new_comment(request, boardid):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        # board_id = Post.objects.get(id=boardid)
        finished_form.post_id = boardid
        finished_form.author_id = request.session['user']
        finished_form.save()

    else:
        print("댓글작성안됨")
        print(boardid)
    return redirect(f'/board/board_detail/{boardid}/')


def update_comment(request, boardid, commentid):
    comment_number = get_object_or_404(Comment, id=commentid)
    get_form = CommentForm(instance=comment_number)
    if request.method == "POST":
        update_form = CommentForm(request.POST, instance=comment_number)
        if update_form.is_valid():
            update_form.save()
            return redirect(f'/board/board_detail/{boardid}/')
    if comment_number.author.email == request.session['user']:
        return render(request, 'user/update_comment.html', {'get_form': get_form})
    else:
        return redirect(f'/board/board_detail/{boardid}/')


def delete_comment(request, boardid, commentid):
    comment_number = get_object_or_404(Comment, id=commentid)
    if comment_number.author.email == request.session['user']:
        comment_number.delete()
        return redirect(f'/board/board_detail/{boardid}/')
    else:
        print("아이디 틀림")
        return redirect(f'/board/board_detail/{boardid}/')