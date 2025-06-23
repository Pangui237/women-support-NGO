from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Event, Category

@login_required
def event_list(request):
    events = Event.objects.all().order_by('-created_at')
    return render(request, 'events/list.html', {'events': events})


@login_required
def event_create(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        time = request.POST.get('time')
        location = request.POST.get('location')
        description = request.POST.get('description')
        mission = request.POST.get('mission')
        requirements = request.POST.get('requirements')
        category_id = request.POST.get('category')
        image = request.FILES.get('image')

        category = Category.objects.get(id=category_id) if category_id else None

        Event.objects.create(
            title=title,
            date=date,
            time=time,
            location=location,
            description=description,
            mission=mission,
            requirements=requirements,
            category=category,
            image=image
        )
        return redirect('event_list')

    return render(request, 'events/form.html', {'categories': categories})


@login_required
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    categories = Category.objects.all()

    if request.method == 'POST':
        event.title = request.POST.get('title')
        event.date = request.POST.get('date')
        event.time = request.POST.get('time')
        event.location = request.POST.get('location')
        event.description = request.POST.get('description')
        event.mission = request.POST.get('mission')
        event.requirements = request.POST.get('requirements')
        category_id = request.POST.get('category')
        event.image = request.FILES.get('image') or event.image

        event.category = Category.objects.get(id=category_id) if category_id else None
        event.save()
        return redirect('event_list')

    return render(request, 'events/form.html', {'event': event, 'categories': categories})


@login_required
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/delete_confirm.html', {'event': event})
