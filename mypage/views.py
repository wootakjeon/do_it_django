from django.shortcuts import render


# Create your views here.
def mypageIndex(request):
    return render(request, 'mypage/index.html')


def mypageAdmin(request):
    return render(request, 'mypage/myadminmain.html')
