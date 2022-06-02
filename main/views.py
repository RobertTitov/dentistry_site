from django.shortcuts import render, get_object_or_404
from.models import Prices, Cotegory

def index(request):
    return render(request, 'main/index.html')

def price(request):
    price_list = Prices.objects.all()
    return render(request, 'main/price.html', {'title' : 'Цены', 'price_list' : price_list})

def category(request, num_cat):
    cat_filt = Prices.objects.filter(cat_id = num_cat)
    # category = Cotegory.objects.get(id = num_cat)
    category = get_object_or_404(Cotegory, pk = num_cat)

    context = {
        'cat_filt' : cat_filt,
        'category' : category,
    }
    
    return render(request, 'main/category.html', context)








    