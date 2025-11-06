from django.shortcuts import render
from .models import Item, Category
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all()

    context = {
        'items' : items,
        'categories': categories
    }

    return render(request, 'store/home.html', context)

def contact(request):
    context = {
        'msg': 'Quieres otros productos contactame!'
    }

    return render(request, 'store/contact.html', context)

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    context={
        'item': item,
        'related_items': related_items
    }

    return render(request, 'store/item.html', context)