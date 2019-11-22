from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostComment
from .forms import PostCommentForm
from django.http import HttpResponseForbidden, HttpResponse
from django.urls import reverse

"""Function view for the home page of the blog. The context """
def home(request):
	context = {
		'posts': Post.objects.all()
	}
	# Rendering the blog home page and taking the context as an argument that displays all the posts.
	return render(request, 'blog/home.html', context)



"""Using class based views for the rest of the blog pages"""
#List the posts
class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	paginate_by = 6



#Individual post view
class PostDetailView(DetailView):
	model = Post

	#Get the context data to be able to display other blogs from within the detail view for the aside in 'post_detail.html'.
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['posts'] = Post.objects.all()[:6]
		return context

		

#Post create class to be used in the form within the 'post_form.html'.
class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    fields = ['title', 'intro', 'content', 'image']
    success_message = 'Your post has been successfully created.'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



#Same as the post create view above. As this view is an update view it will start with information in the create form. The 'LoginRequiredMixin' and 'UserPassesTestMixin' ensures only the user who created the post can access this page.
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = Post
    fields = ['title', 'intro', 'content', 'image']
    success_message = 'Your post has been updated'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #Stop the user from being able to access another users post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False



#View to enable the user who created the post to be able to delete it.
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Post
    success_message = 'Your post has been deleted.'
    success_url = '/blog/'

    #Function to display the message when the post is deleted
    def get_success_message(self, cleaned_data):
        return self.success_message

    #Stop a user from being able to delete another users post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False



#Creating a comment for the posts
@login_required
def post_comment_view(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        try:
            if (request.user.is_authenticated):
                comments = PostComment.objects.all()
                post = get_object_or_404(Post, pk=pk)
                blog = Post.objects.all()
                if request.method == "POST":
                    form = PostCommentForm(request.POST)
                    if form.is_valid():
                        comment = form.save(commit=False)
                        comment.author = request.user
                        comment.post = post
                        comment.save()
                        return redirect('post-detail', pk=post.pk)
                else:
                    form = PostCommentForm()

        except User.DoesNotExist:
            return HttpResponseForbidden()

    return render(request, 'blog/post_comment.html', {'form': form, 'blog': blog, 'comments': comments, 'post': post})



#Allow the comment creator to update the comment
@login_required
def update_post_comment_view(request, pk):
    comments = PostComment.objects.all()
    blog = Post.objects.all()
    comment = get_object_or_404(PostComment, pk=pk)
    if (request.user.is_authenticated and request.user == comment.author or request.user.is_superuser):
        if request.method == "POST":
            form = PostCommentForm(request.POST, request.FILES, instance=comment)
            if form.is_valid():
                comment = form.save()
                return redirect('post-detail', comment.post.id)
        else:
            form = PostCommentForm(instance=comment)
    else:
        return HttpResponseForbidden()

    return render(request, 'blog/post_comment.html', {'form': form, 'blog': blog, 'comments': comments, 'post': comment.post})



#Handle the logic to enable the user to be able to delete a comment
class PostCommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = PostComment
    template_name = 'blog/post_comment_confirm_delete.html'
    success_url = '/blog/'
    fields = ['comment']

    #Stop a user from being able to access another users comment
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        else:
            return False