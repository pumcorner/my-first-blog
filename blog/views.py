from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Personal_info, Comment, Work_detail, Guest_post
from django.shortcuts import render, get_object_or_404
from .form import PostForm,InfoForm,CommentForm,RecordForm,GuestForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    current_posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    info=get_object_or_404(Personal_info)
    return render(request,'blog/homepage.html',{'current_posts':current_posts,'info':info})

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
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_admin(request):
    return render(request, 'blog/error_page.html', {})

@login_required
def post_delete(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('post_list')

def info_detail(request):
    info=get_object_or_404(Personal_info)
    return render(request,'blog/info_detail.html',{'info':info})

@login_required
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

def post_comment(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'blog/comment_detail.html',{'form':form})

@login_required
def work_detail(request):
    if request.method=="POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            wd = form.save(commit = False)
            wd.save()
            return redirect('info_detail')
    else:
        form =  RecordForm()
    return render(request,'blog/work_detail.html',{'form':form})

@login_required
def comment_delete(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.delete()
    return redirect('post_detail',pk=comment.post.pk)
@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

def post_list_new(request):
    return render(request,'blog/post_list_new.html')



#This part is useless
def add_guest_post(request):
    if request.method == "POST":
        form = GuestForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
@login_required
def guest_post_delete(request,pk):
    post = get_object_or_404(Guest_post,pk=pk)
    post.delete()
    return redirect('post_detail')
@login_required
def guest_post_approve(request,pk):
    post=get_object_or_404(Guest_post,pk=pk)
    post.approve()
    return redirect('post_list')
