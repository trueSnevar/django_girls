from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	print("hule nada?")

	return render(request, 'blog/post_list.html', {"posts": posts})

def post_details(request, pk):
	print("hule tobi nada?")
	post = get_object_or_404(Post, pk=pk)
	print("hule tobi nada?")
	return render(request, 'blog/post_details.html', {'post': post})
