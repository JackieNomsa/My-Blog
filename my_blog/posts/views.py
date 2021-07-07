from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Posts, Comments
from .forms import CreatePost, CreateComment


# Create your views here.

def home(request):
    my_posts = Posts.objects.all().order_by('title')
    return render(request, 'posts/home.html', {'data_': my_posts})


def about(request):
    return render(request, 'posts/about.html')

def interests(request):
    my_interests = Posts.objects.filter(title__contains='coding')
    return render(request, 'posts/interests.html',{'data_':my_interests})

def current(request,id):
    post = Posts.objects.filter(id=id)
    return render(request,'posts/currentpost.html',{'post':post})

def add_post(request):
    if request.method == 'POST':
        form = CreatePost(request.POST, request.FILES)

        if form.is_valid():
            t = form.cleaned_data['title']
            p = form.cleaned_data['post']
            a = form.cleaned_data['author']
            m = form.cleaned_data['my_image']

            my_p = Posts(title=t,post=p,author=a, my_image=m)
            my_p.save()
            return redirect('/')
    else:
        form = CreatePost()
    return render(request,'posts/add.html',{'form':form})

def delete_post(request,id):
    post_id = id
    Posts.objects.filter(id=post_id).delete()
    return redirect('/')

def comment_post(request,id):
    post = Posts.objects.get(id=id)
    
    comments = Comments.objects.filter(for_post=id)
    # context = {
    #     'post':post,
    #     'comment':comments,
    # }
    
    if request.method == 'POST':
        form = CreateComment(request.POST)
        if form.is_valid():
            comment = form.cleaned_data['comment']

            user_comment = Comments(comment=comment,for_post=post,written_by='annonymous')

            user_comment.save()
            return render(request,'posts/currentpost.html',{'post':post,
        'comments':comments})
    else:
        form = CreateComment()
        return render(request,'posts/comment.html',{'post':post,'form':form})

def edit_post(request,id):
    current_post = Posts.objects.get(pk=id)
    data = {
        'title':current_post.title,
        'post':current_post.post,
        'author':current_post.author,
        'my_image':current_post.my_image
    }
    my_form = CreatePost(data,initial=data)
    
    return redirect('/add/',{'form':my_form})
