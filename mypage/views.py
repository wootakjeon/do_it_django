import bcrypt
from django.shortcuts import render, redirect
from user.models import User

from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from .room_join import RoomJoin
from .chat_room_service import get_an_chat_room_list, get_chat_room_user, confirm_user_chat_room_join, \
    creat_an_chat_room, creat_an_room_join
from .message_service import get_an_message_list

from collections import Counter
from .room import Room
from .room_join import RoomJoin


# Create your views here.
def mypageIndex(request):
    return render(request, 'mypage/mypage.html')


def lecture(request, ):
    return render(request, "mypage/lecture.html")


def lectureDelete(request, ):
    return render(request, "mypage/lectureDelete.html")


def mypageAdmin(request):
    return render(request, 'mypage/myadminmain.html')


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
                user.password = hashed_password.decode('utf=8')
                user.save()
                return redirect('mypage')

            return render(request, "mypage/password.html")
    else:
        return render(request, 'mypage/password.html')


def userinfoUpdate(request):
    userinfo_object = User.objects.get(email=request.session['user'])
    return render(request, 'mypage/userinfo.html', {'userinfo': userinfo_object})


def userinfoUpdateUpdate(request):
    if request.method == 'POST':
        if User.objects.filter(email=request.session['user']):
            user = User.objects.get(email=request.session['user'])
            user.name = request.POST['name']
            user.nickname = request.POST['nickname']
            user.tel = request.POST['phonenumber1'] + '-' + request.POST['phonenumber2'] + '-' + request.POST[
                'phonenumber3']
            user.save()
            return redirect('userinfoUpdate')
        return render(request, 'mypage/userinfo.html')
    else:
        return render(request, 'mypage/userinfoUpdate.html')


def reservationChat(request):
    mentoUser = User.objects.filter(role='Mentor')
    return render(request, 'mypage/reservationChat.html', {'mentoUser': mentoUser})


def chat_index(request):
    return render(request, 'mypage/chat/chat_index.html', {})


def room(request, room_name):
    userinfo_object = User.objects.get(email=request.session['user'])
    return render(request, 'mypage/chat/room.html', {'room_name': room_name, 'userinfo_object': userinfo_object})


# Create your views here. / views 호출하려면 매핑되는 URLconf 필요
# chat_view 함수를 호출하면 chat.html 을 렌더해주는 함수
def chat_view(request: HttpRequest) -> HttpResponse:
    # 사용자가 있는지 없는지 판단
    user = request.User.is_authenticated
    # 사용자가 있으면 사용자가 속해있는 채팅방 list 표시
    if user:
        # 유저가 참여하고 있는 채팅방 목록(roomJoin 쿼리)
        chat_room_list = get_an_chat_room_list(request.User.email)

        chat_info = {}
        for chat_room in chat_room_list:
            room_id = chat_room.room_id.id
            # 채팅방에 참여중인 유저 list(roomJoin 쿼리)
            chat_user_list = get_chat_room_user(room_id)

            username_list = []
            for chat_user in chat_user_list:
                username = chat_user.email.username
                username_list.append(username)

            # chat_info 변수에 딕셔너리 형태로 저장
            chat_info[room_id] = username_list

        if chat_info == {}:
            chat_info = None

        return render(request, "mypage/chat/chat.html", {'chat_info': chat_info})
    # 사용자가 없으면 로그인화면
    else:
        return redirect(("login"))


# room 함수를 호출하면 room.html 을 렌더해주는 함수 / dict 형태로 room_name value 를 전송
def room_view(request: HttpRequest, room_name: str) -> HttpResponse:
    room_id = str(room_name)
    try:
        confirm_user_chat_room_join(request.user.id, room_id)

        message = get_an_message_list(room_id)

        return render(request, "mypage/chat/room.html", {"room_name": room_name, "message": message})

    except:
        return redirect(("/chat"))


def api_create_room(request: HttpRequest, user_id: str) -> HttpResponse:
    user1 = User.objects.get(email=user_id)
    session = request.session['user']
    user2 = User.objects.get(email=session)

    find_room_qs = RoomJoin.objects.filter(user_id__in=[user1.email, user2.email])
    # 이러면 1번 유저가 참여한 모든 방, 2번 유저가 모두 참여한 방 가져옴

    find_room_list = []
    for find_room in find_room_qs:
        find_room_list.append(find_room.room_id)

    result = Counter(find_room_list)
    for key, value in result.items():
        if value >= 2:
            return redirect(("/chat/" + str(key.id)))

    room = creat_an_chat_room()
    room_id = room.id
    creat_an_room_join(user1, user2, room)

    return redirect(("/chat/" + str(room_id)))
