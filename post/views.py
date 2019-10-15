from django.shortcuts import render, HttpResponse, get_object_or_404,HttpResponseRedirect,redirect,Http404
from .models import *
from .forms import PostForm, CommentsForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


# Create your views here.

def post_index(request):
    postlar = Post.objects.all()
    query = request.GET.get('q')
    if query:
        postlar = postlar.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).distinct()
        

    paginator = Paginator(postlar, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        postlar = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        postlar = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        postlar = paginator.page(paginator.num_pages)

    context = {
        'posts':postlar
    }
    return render(request,'post/index.html', context)


def post_detail(request,id):
    post_det = get_object_or_404(Post,id=id)
    form = CommentsForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post_det
        comment.save()
        return HttpResponseRedirect(post_det.get_absolute_url())
    context = {
        'post':post_det,
        'form':form,
    }
    return render(request,'post/detail.html',context)


def post_create(request):
    if not request.user.is_authenticated:
        return Http404()
    form_cr = PostForm(request.POST or None, request.FILES or None)
    
    if form_cr.is_valid():
        post_cr = form_cr.save(commit=False)
        post_cr.user = request.user
        post_cr.save()
        messages.success(request,'Your post has been created succesfully')
        return redirect(post_cr.get_absolute_url())

    context = {
        'form':form_cr
    }
    
    
    return render(request, 'post/form.html', context)


def post_update(request,id):
    if not request.user.is_authenticated:
        return Http404()
    post_det = get_object_or_404(Post,id=id)
    form_cr = PostForm(request.POST or None, request.FILES or None,instance=post_det)
    if form_cr.is_valid():
        form_cr.save()
        messages.success(request,'Your post has been updated succesfully')
        return HttpResponseRedirect(post_det.get_absolute_url())

    
    context = {
        'form':form_cr
    }
    return render(request, 'post/form.html',context)

def post_delete(request,id):
    if not request.user.is_authenticated:
        return Http404()
    post_det = get_object_or_404(Post, id=id)
    post_det.delete()
    return redirect('post:index')

