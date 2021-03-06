from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from .models import Post, Category, Tag
from main.views import get_client_ip


class TagView:
    def get_tags(self):
        return Tag.objects.order_by('-id')

class CategoryView:
    def category(self):
        return Category.objects.all()


class BlogView(TagView, CategoryView, ListView):
    """Основная страница"""

    model = Post
    # Филтруеть посты если пост не черновык то выведёт пост
    queryset = Post.objects.filter(draft=False).order_by('-date')

    # paginate_by = 1
    paginate_by = 6

    # def get_context_data(self, *args, **kwargs):
    #     context = super(BlogView, self).get_context_data(**kwargs)
    #     context['tag_list'] = Tag.objects.order_by('-id')
    #     return context

def detailViewPost(request, category_url, url):
    """Подробный просмотр поста"""
    # location = request.geolocation
    # print(location)

	# получает обект
    post = Post.objects.get(url=url)
    
    query = Post.objects.filter(draft=False).order_by('-date')[:6]

    categories = Category.objects.all()

    get_client_ip(request)

    return render(request, 'blog/post.html',
        {'el': post,
		'title': 'Подробный просмотр поста',
        'post_list': query,
        'category': categories,
        'nav_name': post.title})

    if request.method == 'POST':
        review = Reviews(
            email=request.POST['email'],
            name=request.POST['name'],
            text=request.POST['text']
            )
        review.save()

        return redirect(post.get_absolute_url)

class CategoriesView(ListView):
    
    model = Category
    # Филтруеть посты если пост не черновык то выведёт пост
    queryset = Category.objects.order_by('-id')
