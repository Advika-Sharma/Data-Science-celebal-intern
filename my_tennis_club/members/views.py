from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm

# List all members
def members_list(request):
    members = Member.objects.all()
    return render(request, 'members_list.html', {'members': members})

# Add a new member
def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members')  # Make sure this name matches your URL pattern
    else:
        form = MemberForm()
    return render(request, 'add_member.html', {'form': form})
from django.shortcuts import get_object_or_404

def delete_member(request, id):
    member = get_object_or_404(Member, id=id)
    member.delete()
    return redirect('members')  # or redirect to the appropriate view
