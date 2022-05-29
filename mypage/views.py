import bcrypt
from django.shortcuts import render, redirect
from user.models import User

# Create your views here.
def mypageIndex(request):
    return render(request, 'mypage/mypage.html')


def mypageAdmin(request):
    return render(request, 'mypage/myadminmain.html')


def consulting(request):
    return render(request, 'mypage/consulting.html')


def passwordUpdate(request):
    session_user = request.session['user']
    print("session_user", session_user)

    if request.method == 'POST':
        if User.objects.filter(email=session_user).exists():
            user = User.objects.get(email=session_user)
            user_password = user.password.encode('utf=8')

            if bcrypt.checkpw(request.POST['nowpwd'].encode('utf=8'), user_password):
                update_password = request.POST['updatepwd']
                hashed_password = bcrypt.hashpw(update_password.encode('utf=8'), bcrypt.gensalt())
                user.password=hashed_password.decode('utf=8')
                user.save()
                return redirect('mypage')

            return render(request, "mypage/password.html")
    else:
        return render(request, 'mypage/password.html')


def userinfoUpdate(request):
    userinfo_object = User.objects.get(email=request.session['user'])
    return render(request, 'mypage/userinfo.html', {'userinfo':userinfo_object})


def userinfoUpdateUpdate(request):
    if request.method == 'POST':
        if User.objects.filter(email=request.session['user']):
            user = User.objects.get(email=request.session['user'])
            user.name = request.POST['name']
            user.nickname = request.POST['nickname']
            user.tel = request.POST['phonenumber1']+'-'+request.POST['phonenumber2']+'-'+request.POST['phonenumber3']
            user.save()
            return redirect('userinfoUpdate')
        return render(request, 'mypage/userinfo.html')
    else:
        return render(request, 'mypage/userinfoUpdate.html')

