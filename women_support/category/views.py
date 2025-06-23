from django.shortcuts import render, redirect, get_object_or_404
from .models import Category
from django.contrib.auth.decorators import login_required

@login_required
def category_list(request):
    categories = Category.objects.all().order_by('-created_at')
    return render(request, 'category/list.html', {'categories': categories})

@login_required
def category_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name:
            Category.objects.create(name=name, description=description)
            return redirect('category_list')
    return render(request, 'category/create.html')

@login_required
def category_edit(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name:
            category.name = name
            category.description= description
            category.save()
            return redirect('category_list')
    return render(request, 'category/edit.html', {'category': category})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'category/delete.html', {'category': category})
