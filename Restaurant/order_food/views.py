from django.shortcuts import render
from . models import Comment
def home_page(request):

    if request.method == 'POST':
        food_name = request.POST.get('food_name')
        address = request.POST.get("address")
        order_obj = Comment.objects.create(
            food = food_name,
            address = address,
        )
        return render(request, 'order_food/home_page.html', {'foods': order_obj})

    return render(request, 'order_food/home_page.html')