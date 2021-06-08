from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Posts
from .forms import CreatePost
from .serializer import PostSerializer

# Create your views here.

def home(request):
    my_posts = Posts.objects.all().order_by('title')
    return render(request, 'posts/home.html', {'data_': my_posts})


def about(request):
    return render(request, 'posts/about.html')

def interests(request):
    my_interests = Posts.objects.filter(title__contains='coding')
    return render(request, 'posts/interests.html',{'data_':my_interests})


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
    else:
        form = CreatePost()
    return render(request,'posts/add.html',{'form':form})

def delete_post(request,id):
    post_id = int(id)

    Posts.objects.filter(id=post_id).delete()
    return redirect('home')

def comment_post(request,id):
    return redirect('home')

def edit_post(request,id):
    return redirect('home')
# def post_details(request,pk):
#     '''retrieve update delete post'''
#     try:
#         post = Posts.objects.get(pk=pk)
#     except Posts.DoesNotExist:
#         print('post does not exist')

#     if request.method == 'PUT':
#         serializer = PostSerializer(post,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
        
#     elif request.method == 'DELETE':
#         post.delete()

#     return render('home')