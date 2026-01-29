from django.shortcuts import get_object_or_404, render ,redirect
from.models import Post,Catagory,Tag,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from .forms import PostForm,CommentForm,UpdateProfileForm
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

def post_list(request):
    catagoryQ=request.GET.get('category')
    tagQ=request.GET.get('tag')
    searchQ=request.GET.get('q')
    
    posts=Post.objects.all()
    
    if catagoryQ:
        posts=posts.filter(Catagory__name=catagoryQ)
    if tagQ:
        posts=posts.filter(tags__name=tagQ) 
    if searchQ: 
        posts=posts.filter(
            Q(title__icontains=searchQ) | Q(content__icontains=searchQ)
            | Q(tags__name__icontains=searchQ) | Q(Catagory__name__icontains=searchQ)
        ).distinct()

    paginator=Paginator(posts,2)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    
    context={
      "page_obj":page_obj,
      "catagories":Catagory.objects.all(),
      "tags":Tag.objects.all(),
      "search_query":searchQ,
      "catagory_query":catagoryQ,
      "tag_query":tagQ,

    }
    return render(request,'blog/post_list.html',context)
def post_detail(request,id):
    post=get_object_or_404(Post,id=id)
    if request.method=='POST':
        comment_from=CommentForm(request.POST)
        if comment_from .is_valid():
           comment=comment_from.save(commit=False)
           comment.post=post
           comment.author=request.user
           comment.save()    
           return redirect('post_detail',id=post.id)
    else:
        comment_from=CommentForm()

    comments=post.comment_set.all().order_by('-created_at')
    is_liked=post.liked_users.filter(id=request.user.id).exists()
    like_count=post.liked_users.count()

    context={
        "post":post,
        "catagoeries":Catagory.objects.all(),
        "tag":Tag.objects.all(),
        "comments":comments,
        "comment_form":comment_from,
        "is_liked":is_liked,
        "like_count":like_count,
    }
    post.view_count +=1
    post.save()
    return render(request,'blog/post_detail.html',context)

@login_required
def like_post(request,id):
    post=get_object_or_404(Post,id=id)
    if post.liked_users.filter(id=request.user.id).exists():
        post.liked_users.remove(request.user)
    else:
        post.liked_users.add(request.user)
    return redirect('post_list')

@login_required
def post_create(request):
   if request.method=='POST':
      form= PostForm(request.POST)
      if form.is_valid():
          post=form.save(commit=False)
          post.author=request.user
          post.save()
          return redirect('post_detail',id=post.id)
   else:
         form=PostForm()
    
   return render(request,'blog/post_create.html',{'form': form})

@login_required
def post_update(request,id):
   post=get_object_or_404(Post,id=id)
   if request.method=='POST':
      form= PostForm(data=request.POST,instance=post)
      if form.is_valid():
          post.save()
          return redirect('post_detail',id=post.id)
   else:
         form=PostForm(instance=post)
    
   return render(request,'blog/post_create.html',{'form': form})

@login_required
def post_delete(request, id):
    post=get_object_or_404(Post,id=id)
    post.delete()
    return redirect('post_list')

def signup_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login (request,user)
            return redirect('post_list')
    else:
        form=UserCreationForm()
    return render (request,'user/signup.html',{'form':form})

@login_required
def profile_view(request):
    section= request.GET.get('section','profile')
    context={
        'section':section,
    }
    if section=='posts':
        posts=Post.objects.filter(author=request.user)
        context['posts']=posts
    elif section=='update':
        if request.method=='POST':
            form = UpdateProfileForm(request.POST,instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('/profile/?section=update')
        else:
            form = UpdateProfileForm(instance=request.user)

        context['form']=form
    return render (request,'user/profile.html',context)
