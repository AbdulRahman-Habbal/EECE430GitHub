from django.shortcuts import render, redirect, get_object_or_404
from .models import Video
from .forms import VideoForm

def video_list(request):
    videos = Video.objects.all().order_by('-ReleaseYear')
    return render(request, 'inventory/video_list.html', {'videos': videos})

def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'inventory/video_detail.html', {'video': video})

def video_create(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'inventory/video_form.html', {'form': form, 'title': 'Add New Video'})

def video_update(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        form = VideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('video_detail', pk=video.MovieID)
    else:
        form = VideoForm(instance=video)
    return render(request, 'inventory/video_form.html', {'form': form, 'title': 'Edit Video'})

def video_delete(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        video.delete()
        return redirect('video_list')
    return render(request, 'inventory/video_confirm_delete.html', {'video': video})
