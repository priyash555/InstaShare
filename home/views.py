from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
def starting(request):
    return render(request,'home/starting.html',{})

class PostListView(ListView):
    model = Post
    template_name = 'home/starting.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class ModelCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "home/createpost.html"
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    
class ModelUpdateView(LoginRequiredMixin, UserPassesTestMixin ,CreateView):
    model = Post
    template_name = "home/createpost.html"
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class ModelDetailView(DetailView):
    model = Post
    template_name = "home/detail.html"

class ModelDeleteView(LoginRequiredMixin, UserPassesTestMixin , DeleteView):
    model = Post
    template_name = "home/delete.html"
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    
class UserListView(ListView):
    model = Post
    template_name = 'home/user_post.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    
    def get_queryset(self):
        user = get_object_or_404(User , username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
def about(request):
    return render(request, 'home/about.html', {})