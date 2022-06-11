from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from mentor.models import Mentor


def mentor(request):
    mentorList = Mentor.objects.all().order_by('id')
    page = request.GET.get('page', '1')
    paginator = Paginator(mentorList, 16)
    page_obj = paginator.get_page(page)

    context = {'mentorList': page_obj}
    return render(request, 'mentor/mentor.html', context)


def mentor_up(request):
    if request.method == 'POST':
        Mentor(
            mentor=request.POST['mentor'],
            mentor_img=request.FILES['mentor_img'],
            mento_title=request.POST['mento_title'],
            mento_content=request.POST['mento_content'],
            mento_field=request.POST['mento_field']
        ).save()
        return redirect('mentor')
    return render(request, 'mentor/mentor_upload.html')


def mentor_content(request):
    return render(request, 'mentor/mentor_content.html')

def mentor_profile(request):
    return render(request, 'mentor/mentor_profile.html')