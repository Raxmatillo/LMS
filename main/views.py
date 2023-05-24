from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from accounts.forms import EditProfileForm
from .models import Department, Topic


@login_required(login_url='account/login')
def home_view(request):
    departments = Department.objects.all()
    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Ma'lumotlar muvaffaqiyatli saqlandi.")
            return redirect("home")

    context = {
        'departments': departments
    }
    return render(request, 'index.html', context)


@login_required(login_url='account/login')
def detail_view(request, pk):
    topic = Topic.objects.get(pk=pk)
    departments = Department.objects.all()
    context = {
        'topic': topic,
        'departments': departments
    }
    return render(request, 'detail_topic.html', context)


def my_view(request):
    query = request.GET.get('q')
    if query:
        instances = Topic.objects.filter(
            Q(titleicontains=query) | Q(bodyicontains=query) |
            Q(department__name__icontains=query) | Q(bodyicontains=query)
        )
    else:
        instances = Topic.objects.none()

    context = {'instances': instances}
    return render(request, 'search_results.html', context)