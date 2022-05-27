import bcrypt
import jwt
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
import user
from do_it_django_prj.settings import SECRET_KEY
from .models import User
from .models import Post
from .forms import BoardWriteForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator


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
                role=request.POST['gender']
            ).save()
            return redirect('login')
        return render(request, 'user/join.html')
    else:
        form = UserCreationForm
        return render(request, 'user/join.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('login')


def board(request):
    boards = Post.objects.all().select_related('author').order_by('id')
    page = request.GET.get('page', 1)
    paginator = Paginator(boards, 5)
    board_list = paginator.get_page(page)
    return render(request, 'user/board.html', {'boards': boards, 'board_list': board_list})


def board_write(request):
    login_session = request.session.get('login_session', '')
    context = {'login_session': login_session}

    if request.method == 'GET':
        write_form = BoardWriteForm()
        context['forms'] = write_form
        return render(request, 'user/board_write.html', context)

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
            return redirect('/board')
        else:
            context['forms'] = write_form
            if write_form.errors:
                for value in write_form.errors.values():
                    context['error'] = value
            return render(request, 'user/board_write.html', context)


def board_detail(request, boardid):

    board = get_object_or_404(Post, pk=boardid)
    session = request.session['user']

    context = {
        'board': board,
        'session': session
               }
    return render(request, 'user/board_detail.html', context)


    context['board'] = board

    return render(request, 'user/board_detail.html', context)
