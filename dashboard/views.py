from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    if request.user.is_superuser == True:
        return redirect('admin:index')
    else:
        return render(request, 'dashboard/dashboard.html')