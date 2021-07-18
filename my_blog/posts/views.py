from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Posts, Comments
from .forms import CreatePost, CreateComment


def home(request):
    my_posts = Posts.objects.all().order_by('title')
    
    
    return render(request, 'posts/home.html', {'data_': my_posts})


def about(request):
    return render(request, 'posts/about.html')

def interests(request):
    my_interests = Posts.objects.filter(title__contains='coding')
    return render(request, 'posts/interests.html',{'data_':my_interests})

def current(request,id):
    post = Posts.objects.get(id=id)
    comments = Comments.objects.filter(for_post_id=id)
    return render(request,'posts/comment.html',{'post':post,'comments':comments})

def add_post(request):
    if request.user.is_authenticated():

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
        return render(request,'posts/add.html',{'form':form,'title':'Create Post','button':'Add Post'})
    return render(request,'accounts/login.html',{'context':'please sign up or login to add/comment blog'})
    
def delete_post(request,id):
    post_id = id
    Posts.objects.filter(id=post_id).delete()
    return redirect('/')

def comment_post(request,id):
    post = Posts.objects.get(id=id)
    
    current_comments = Comments.objects.filter(for_post_id=post.id)
    
    
    if request.method == 'POST':
        form = CreateComment(request.POST)
        
        if form.is_valid():
            comment = form.cleaned_data['comment']
            writer = form.cleaned_data['written_by']

            user_comment = Comments(comment=comment,for_post=post,written_by=writer)

            user_comment.save()
            return render(request,'posts/comment.html',{'post':post,
        'comments':current_comments})
    else:
        form = CreateComment()
        return render(request,'posts/comment.html',{'post':post,'form':form,'comments':current_comments})

def edit_post(request,id):
    current_post = Posts.objects.get(pk=id)

    form = CreatePost(instance=current_post)
    if request.method == 'POST':
        form = CreatePost(request.POST,instance=current_post)

        if form.is_valid():
            print(form)
            current_post.title = form.title
            current_post.post = form.post
            current_post.author = form.author
            current_post.save()
        return redirect('/')
    
    return render(request,'posts/add.html',{'form':form,'title':'Edit Post','button':'Update'})

def delete_comment(request,id):
    comment = Comments.objects.get(id=id)
    # post = Posts.objects.get(id=comment.for_post_id)
    comment.delete()
    
    return redirect('current')
