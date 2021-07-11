from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Posts, Comments
from .forms import CreatePost, CreateComment


# Create your views here.

# my_comments = Comments.objects.all()
# my_post_comments = []

# for p in Posts.objects.all():
    
#     for c in my_comments:
#         if p.id == c.for_post_id:
#             my_post_comments.append({p.title:c.for_post_id})

# my_counter = 0
# while my_counter < len(my_post_comments):
#     if

# print(my_post_comments)

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
    
    current_comments = Comments.objects.filter(for_post_id=post.id)
    
    
    if request.method == 'POST':
        form = CreateComment(request.POST)
        
        if form.is_valid():
            comment = form.cleaned_data['comment']

            user_comment = Comments(comment=comment,for_post=post,written_by='annonymous')

            user_comment.save()
            return render(request,'posts/currentpost.html',{'post':post,
        'comments':current_comments})
    else:
        form = CreateComment()
        return render(request,'posts/comment.html',{'post':post,'form':form})

def edit_post(request,id):
    current_post = Posts.objects.get(pk=id)
    
    my_form = CreatePost(instance=current_post)

    
    
    return render(request,'posts/add.html',{'form':my_form})

def delete_comment(request,id):
    comment_id = id
    current_comment = Comments.objects.filter(id=comment_id)
    current_post = Posts.objects.get(id=current_comment.for_post)
    Comments.objects.filter(id=comment_id).delete()
    
    return render(request,'posts/currentpost.html',{'post':Posts.objects.get()})
