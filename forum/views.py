from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Thread, Post
from .forms import CategoryForm, ThreadForm, PostForm
from .tables import ThreadsTable
from samples.views import add_edit_instance
from django.contrib import messages

def forum(request):
    categories = Category.objects.all()
    return render(request, 'forum/categories.html', {'categories': categories})

def add_edit_category(request, pk=None):
    category = get_object_or_404(Category, id=pk) if pk else None
    action = 'edited' if pk else 'added'
    return add_edit_instance(
        request=request,
        form=CategoryForm,
        instance=category,
        redirect_url='forum',
        type='Category',
        action=action
        )

def threads(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    threads = Thread.objects.filter(category=category)
    table = ThreadsTable(threads)
    return render(request, 'forum/threads.html', {'id': category.id,'name':category.name, 'table': table})

def add_edit_thread(request, category_id, pk=None):
    # Fetch the category for the thread
    category = get_object_or_404(Category, id=category_id)

    # If editing, fetch the existing thread; otherwise, create a new one
    if pk:
        thread = get_object_or_404(Thread, id=pk)
        action = 'edited'
    else:
        thread = None
        action = 'added'

    if request.method == 'POST':
        if 'delete' in request.POST:
            if thread:
                thread.delete()
                messages.success(request, f"Thread {action} successfully!")
                return redirect('threads', category_id=category.id)
        else:
            form = ThreadForm(request.POST, instance=thread)
            if form.is_valid():
                # Save the form, which will ensure the category and author are set
                thread = form.save(commit=False)
                thread.category = category
                thread.author = request.user  # Automatically set the current user as the author
                thread.save()
                messages.success(request, f"Thread {action} successfully!")
                return redirect('threads', category_id=category.id)
    else:
        form = ThreadForm(instance=thread)

    return render(request, 'add_edit_instance.html', {
        'form': form, 
        'instance': thread, 
        'type': 'Thread'
    })

def delete_threads(request):
    if request.method == "POST":
        threads_to_delete = request.POST.getlist('threads_to_delete')
        if threads_to_delete:
            threads = Thread.objects.filter(id__in=threads_to_delete)
            category = threads.first().category
            threads.delete()
        return redirect('threads', category_id=category.id)  

    return redirect('threads', category_id=category.id)

def posts(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    posts = Post.objects.filter(thread=thread)
    form = PostForm(initial={'thread': thread})
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post added successfully!")
            return redirect('posts', thread_id=thread.id)
    return render(request, 'forum/posts.html', {'form': form, 'posts': posts, 'thread_id': thread_id})


    