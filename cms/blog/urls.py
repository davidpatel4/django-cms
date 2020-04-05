from django.urls import path ,re_path
from blog.views import index
from blog.views import post_details,contact_view,post_form_view,post_edit_form_view,PostListView,PostDetailView,PostFormView,ContactFormView,PostFormUpdateView


urlpatterns = [
    # path('',index),
    path('',PostListView.as_view()),
    # path("<int:id>",post_details),
    # path("<int:pk>",PostDetailView.as_view()),
    path("posts",PostFormView.as_view()),
    path("posts/<slug:slug>",PostFormUpdateView.as_view()),
    path("contact",ContactFormView.as_view()),
    path("<slug:slug>",PostDetailView.as_view(),name ="post-detail"),
    # path("contact",contact_view),
    
    # path("posts",post_form_view),


]

# "post-detail" => "<slug:slug>"

# url "post-detail" "abc" = "/abc" => valid url 
# a= 10 
# print(a)

# post-detail = "post/<slug:slug>""

# {% url 'url_name' args %}

# reverse('post-detail',kwargs = {'slug':})
# reverse_lazy('post-detail',kwargs = {'slug':})

