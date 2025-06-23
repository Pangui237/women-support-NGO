from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Donation
from decimal import Decimal

# List donations
def donation_list(request):
    donations = Donation.objects.all().order_by('-created_at')
    return render(request, 'donations/list.html', {'donations': donations})

# Create donation
def donation_create(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        goal_amount = Decimal(request.POST.get('goal_amount') or 0)
        raised_amount = Decimal(request.POST.get('raised_amount') or 0)
        image = request.FILES.get('image')

        category = Category.objects.get(id=category_id) if category_id else None

        Donation.objects.create(
            title=title,
            description=description,
            category=category,
            goal_amount=goal_amount,
            raised_amount = raised_amount,
            image=image
            
        )
        return redirect('donation_list')

    return render(request, 'donations/form.html', {'categories': categories})

# Edit donation
def donation_edit(request, pk):
    donation = get_object_or_404(Donation, pk=pk)
    categories = Category.objects.all()

    if request.method == 'POST':
        donation.title = request.POST.get('title')
        donation.description = request.POST.get('description')
        category_id = request.POST.get('category')
        donation.goal_amount = Decimal(request.POST.get('goal_amount') or 0)
        donation.raised_amount = Decimal(request.POST.get('raised_amount') or 0)

        if request.FILES.get('image'):
            donation.image = request.FILES.get('image')

        donation.category = Category.objects.get(id=category_id) if category_id else None
        donation.save()

        return redirect('donation_list')

    return render(request, 'donations/form.html', {
        'donation': donation,
        'categories': categories
    })

# Delete donation
def donation_delete(request, pk):
    donation = get_object_or_404(Donation, pk=pk)
    donation.delete()
    return redirect('donation_list')

def donations_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    donations = Donation.objects.filter(category=category)
    return render(request, 'donations/list_by_category.html', {
        'donations': donations,
        'category': category
    })
