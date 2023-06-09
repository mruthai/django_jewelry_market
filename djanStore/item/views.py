from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm
from .models import Item, Category

""" Function query items available within our database for user to search"""
def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items =items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description_icontains=query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })


""" Function to add details to each item that is created by the userID """
def detail(request, pk):  #pk is primary key
    item = get_object_or_404(Item, pk=pk) 
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3] #slice only show up to related items

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })  
""" Fuction for user to user to create a new item in a higher level category """
@login_required
def new_user_item(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item',
    })

""" Function to allow the user to edit an item that already exists in their inventory"""

@login_required
def edit(request,pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit Item',
    })
""" Function to allow the user to delete an item they can't sell in from inventory"""
@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')