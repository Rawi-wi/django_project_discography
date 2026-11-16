from django.shortcuts import render, redirect, get_object_or_404
from members.forms import MemberForm
from members.models import Member


def members_list(request):
    members = Member.objects.all()
    return render(request, 'members/member_list.html', {'members': members})


def members_detail(request, pk):
    member = get_object_or_404(Member, pk=pk)
    return render(request, 'members/member_detail.html', {'member': member})


def members_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save()
            return redirect('members:detail', pk=member.pk)
    else:
        form = MemberForm()

    return render(request, 'members/member_form.html', {'form': form})


def members_edit(request, pk):
    member = get_object_or_404(Member, pk=pk)

    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('members:detail', pk=member.pk)
    else:
        form = MemberForm(instance=member)

    return render(request, 'members/member_form.html', {'form': form, 'member': member})
