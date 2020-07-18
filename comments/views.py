from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.contenttypes.models import ContentType
from .models import Comment
from . forms import CommentForm
from django.contrib import messages




# Create your views here.

def comment_thread(request,id):
    obj = get_object_or_404(Comment, id=id)
    content_object =obj.content_object
    content_id = obj.content_object.id
    initial_data = {
        'content_type': obj.content_type,
        'object_id': obj.object_id,
    }

    form = CommentForm(request.POST or None, initial=initial_data)

   
    if form.is_valid():
        c_type = form.cleaned_data.get('content_type')
        content_type = ContentType.objects.get(model=c_type)
        obj_id = form.cleaned_data.get('object_id')
        content_data = form.cleaned_data.get('content')

        parent_obj=None
        try:
            parent_id = request.POST.get('parent_id')
        except:
            parent_id = None


        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists():
                parent_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
            user = request.user,
            content_type = content_type,
            object_id = obj_id,
            content = content_data,
            parent = parent_obj

        )

    context={
        'comment':obj,
        'form':form,
    }
    return render(request,'comment/comment_thread.html', context)

def comment_delete(request, id):
    obj = get_object_or_404(Comment, id=id)
    if request.method =='POST':
        
        obj.delete()
        messages.success(request,'Comment deleted successfully.')
        return render(request,'')

    context ={
        'object':obj,
    }

    return  render(request,'comment/confirm_delete.html', context)
