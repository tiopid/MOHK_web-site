from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Gender


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})


# class GenreYear:
#     """Жанры и года выхода фильмов"""
#     def get_genres(self):
#         return Category.objects.all()
#
#     def get_years(self):
#         return G.objects.filter(draft=False).values("year")