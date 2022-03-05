from django.shortcuts import render, HttpResponse
from .models import Post, user_profile
from django.views import generic 
from Project.settings import STATIC_URL
from django.db.models import Q 
# Create your views here.

class PostList(generic.ListView):
    model = Post
    def get_context_data(self, *args, **kwargs):
      context = super(PostList, self).get_context_data(*args, **kwargs)
      context['count'] = Post.objects.filter(status=1).order_by('-count')[:4]
      context['ordered'] = Post.objects.filter(status=1).order_by('-created_on')      
      return context
    template_name = 'index.html'

class AuthorView(generic.DetailView):
    model = user_profile
    def get_context_data(self, **kwargs):
      context = super(AuthorView, self).get_context_data(**kwargs)
      return context
    template_name = 'author.html'   
     

class SearchResultsView(generic.ListView):
    model = Post
    template_name = 'search_results.html'    
    def get_context_data(self, *args, **kwargs):
      query = self.request.GET.get('search')
      context = super(SearchResultsView, self).get_context_data(*args, **kwargs)
      context['post'] = Post.objects.filter(
            Q(title__icontains=query)| Q(content__icontains=query)
        )
      return context

class DetailView(generic.DetailView):
  model = Post
  def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['ordered'] = Post.objects.filter(status=1).exclude(slug=self.kwargs['slug']).order_by('-created_on')
        self.object.add_visit()
        self.object.save()
        return context
        
  template_name = 'post_detail.html'
  

