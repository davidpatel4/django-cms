from django.shortcuts import render
from django.http import HttpResponse
from blog.forms import ContactForm
from blog.forms import PostForm

from django.views import View
from blog.models import Post,Category
from django.views.generic import ListView,DetailView,FormView,CreateView,UpdateView
# Create your views here.

# def index(request,*args,**kwargs):
#     posts = Post.objects.filter(status = "P")
#     post_titles = [post.title for post in posts]
#     title_str = ("\n\n").join(post_titles)
#     return HttpResponse(title_str)

def index(request,*args,**kwargs):
    posts = Post.objects.filter(status = "P")    
    return render(request,"blog/index.html",context= {"posts":posts})

# class PostListView(View):

#     def get(self,request,*args,**kwargs):
#         posts = Post.objects.filter(status = "P")    
#         return render(request,"blog/index.html",context= {"posts":posts})

class PostListView(ListView):
    model = Post
    queryset = Post.objects.filter(status = "P")
    template_name = "blog/index.html"
    context_object_name = "posts"


    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        # context['author'] = Author.objects.all()

        return context


def post_details(request,id,*args,**kwargs):
    
    
    post = Post.objects.get(id = id)
        
    return render(request,"blog/details.html",context={"post":post})


# class PostDetailView(View):

#     def get(self,request,id,*args,**kwargs):
#         post = Post.objects.get(id = id)
        
#         return render(request,"blog/details.html",context={"post":post})

class PostDetailView(DetailView):
    model = Post
    # queryset = Post.objects.filter(status = "P")
    template_name = "blog/details.html"



def contact_view(request,*args,**kwargs):
    # print(request.GET)
    print(request.POST)
    if request.method == "GET":
        form = ContactForm()
        return render(request,"blog/contact.html",context = {"form":form})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("Thank You")
        else:
            return render(request,"blog/contact.html",context = {"form":form})



    form = ContactForm()
    return render(request,"blog/contact.html",context = {"form":form})


class ContactFormView(FormView):
    form_class = ContactForm
    success_url = "contact"
    template_name = "blog/contact.html"

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)


# class PostFormView(View):
#     def get(self,request,*args,**kwargs):
#         form = PostForm()
#         return render(request,"blog/post.html",context={"form":form})

#     def post(self,request,*args,**kwargs):
#         form = PostForm(request.POST,request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data.get('image').image.__dict__)
#             form.save()
#             return HttpResponse("Thank You")
#         else:
#             return render(request,"blog/post.html",context={"form":form})

class PostFormView(CreateView):
    # model = Post
    # fields = ['title','content','status','category','image']
    # success_url = 'posts'
    template_name = "blog/post.html"
    form_class = PostForm

class PostFormUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post.html"


def post_form_view(request,*args,**kwargs):
    if request.method == "GET":
        form = PostForm()
        return render(request,"blog/post.html",context={"form":form})

    else:
        print(request.POST)
        print(request.FILES)
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data.get('image').image.__dict__)
            form.save()
            return HttpResponse("Thank You")
        else:
            return render(request,"blog/post.html",context={"form":form})


def post_edit_form_view(request,id,*args,**kwargs):
    try :
        post = Post.objects.get(id = id)
    except:
        return HttpResponse("Invalid Post ID")

    if request.method == "GET":
        form = PostForm(instance = post)
        return render(request,"blog/post.html",context = {"form":form})
    else:    

        form = PostForm(request.POST,request.FILES,instance = post)
        if form.is_valid():
            form.save()
                    
        return render(request,"blog/post.html",context = {"form":form})
        
        
# request.FILES
# def post_details(request,id,*args,**kwargs):
#     try:
#         post = Post.objects.get(id = id)
#         post_str = "{} \n\n {}".format(post.title,post.content)
#         return HttpResponse(post_str)
#     except:
#         return HttpResponse("Invalid Id")

# /admin
# /posts


# 127.0.0.1:8000/blogs

# http://127.0.0.1:8000/blogs/

# http://127.0.0.1:8000/blogs/ => cms.url

# "" => blog.urls 

# import re
# [a-z]{3}
# ^[0-9]
# [a-z]$

# (?P<post_id>[0-9])


# localhost/blogs/

# set of URl patterens  => urls.py                              name of the url  => url pattern   => pass the args to contruct the url 

# find the view 

# render a teamplate                                             temaplte 
 



# I am into template  => end goal is to construct an URL 

# 1. Hard coad the url 

# Blogs => blog => detail page for that blog 

# /slug/

# Username , Password 

# user = User(username = username,password = password)
# user.set_password(password)
# user.save()


# user = User.objects.create_user(username=username,password=password)

# abc,abcd@123



# username,password :
# check username

# user = User.ojects.get(username = "abc")
# user.checkpassword(password)


# username abc  123456 
# username abc  abcd 

# user = user.objects.get(username = abc)
# user.checkpassword(abcd)




# from name  => 'post-detail' => pattern "post/<slug:slug>" => pass the args => "posts/intro-to-ai"





# 'post-detail' = ><slug:slug> => pass the args  => "intro-to-ai"





# view : 
# create a url 


# reverse('post-detail',kwargs= {"slug":self.slug})



# post.get_abs_url 


# get_abs_url(post):
#     res "post-detail" , post.slug  => detail page url 



# Template View 
# Delete View 