from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Personal_info
from django.shortcuts import render, get_object_or_404
from .form import PostForm,InfoForm
from django.shortcuts import redirect

# Create your views here.
def homepage(request):
    current_posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    info=get_object_or_404(Personal_info)
    return render(request,'blog/homepage.html',{'current_posts':current_posts ,'info':info})

def post_list(request):
    current_posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request,'blog/post_list.html',{'current_posts':current_posts})

def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_admin(request):
    return render(request, 'blog/error_page.html', {})

def info_detail(request):
    info=get_object_or_404(Personal_info)
    return render(request,'blog/info_detail.html',{'info':info})

def info_edit(request):
    info=get_object_or_404(Personal_info)
    if request.method == "POST":
        form = InfoForm(request.POST, instance=info)
        if form.is_valid():
            info = form.save()
            info.author = request.user
            info.changed_date = timezone.now()
            info.save()
            return redirect('info_detail')
    else:
        form = InfoForm(instance=info)
    return render(request,'blog/info_edit.html',{'form':form})
