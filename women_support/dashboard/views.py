from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    # print("User:", request.user)
    # print("Role:", getattr(request.user, 'role', 'NO ROLE'))
    # print("Is superuser:", request.user.is_superuser)

    role = getattr(request.user, 'role', None)

    if role == 'donor':
        return render(request, 'dashboard/donor_dashboard.html')
    elif role == 'intent':
        return render(request, 'dashboard/intent_dashboard.html')
    elif role == 'mentor':
        return render(request, 'dashboard/mentor_dashboard.html')
    elif role == 'partner':
        return render(request, 'dashboard/partner_dashboard.html')
    elif role == 'volunteer':
        return render(request, 'dashboard/volunteer_dashboard.html')
    elif request.user.is_superuser:
        return render(request, 'dashboard/admin_dashboard.html')

    return redirect('/')
