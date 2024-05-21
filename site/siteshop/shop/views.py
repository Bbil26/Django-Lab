from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import News, ItemShop, Carts

from django.http import HttpResponse


def index(request):
    return render(request, 'shop/index.html')


def news(request):
    articles_list = News.objects.all().order_by("-date", "-title")

    query = request.GET.get('search')
    if query:
        articles_list = articles_list.filter(title__icontains=query)

    paginator = Paginator(articles_list, 3)  # По 3 записи на странице
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # Если страница не является целым числом, показываем первую страницу
        articles = paginator.page(1)
    except EmptyPage:
        # Если страница выходит за пределы диапазона (например, страница 9999),
        # показываем последнюю страницу
        articles = paginator.page(paginator.num_pages)

    return render(request, 'shop/news.html', {'articles': articles})


def news_detail(request, slug):
    news_item = get_object_or_404(News, slug=slug)
    return render(request, 'shop/news_detail.html', {'news_item': news_item})


def add_to_cart(request, item_id):

    if Carts.objects.filter(id_item=item_id).exists():
        return redirect('home')
    else:
        # Получаем товар по его идентификатору
        item = ItemShop.objects.get(id_item=item_id)

        # Создаем запись в корзине
        cart_item, created = Carts.objects.get_or_create(
            id_user=1,  # Здесь указываем id пользователя, для которого добавляем товар
            id_item=item.id_item,
            count=1,
            summary=1
        )
        return redirect('home')



def remove_cart(request, item_id):
    try:
        # Найдите объект корзины, который вы хотите удалить
        cart_item = Carts.objects.filter(id_user=1, id_item=item_id).first()
        # Удалите объект корзины

        if cart_item:
            # Удалите найденный объект корзины
            cart_item.delete()
            return redirect('home')
        else:
            return HttpResponse("Товара нет в корзине")
    except Carts.DoesNotExist:
        return HttpResponse("Товара нет в корзине")


def add_count(request, item_id):
    car = Carts.objects.get(id_user=1, id_item=item_id)
    if car.count + 1 == 11 :
        pass
    else:
        car.count = car.count + 1
        Carts.save(car)
    return redirect('home')


def rem_count(request, item_id):
    car = Carts.objects.get(id_user=1, id_item=item_id)
    if car.count - 1 == 0:
        remove_cart(request, item_id)
    else:
        car.count = car.count - 1
        Carts.save(car)
    return redirect('home')

