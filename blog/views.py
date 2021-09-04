from django.shortcuts import redirect, render
from django.views.generic import ListView
from .models import CreateBlog, Comment
from .forms import BlogForm

class List(ListView):
    template_name = 'blog/index.html'
    queryset = CreateBlog.objects.all()
    paginate_by = 3


def detailView(request, slug):
    post = CreateBlog.objects.get(slug=slug)
    comments = post.comments.all()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.post = post
            form.save()
            return redirect('detailView', slug=post.slug)
    else:
        form = BlogForm()

    content = {
        'article':post,
        'comments':comments,
        'form':form,

    }
    return render(request, 'blog/update.html', content)
     