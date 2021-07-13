from django.shortcuts import get_object_or_404, render
from .models import YouTuber

# Create your views here.
def youtubers(request):
    tubers = YouTuber.objects.order_by('created_date')
    data = {
        'tubers':tubers
    }
    return render(request, 'youtubers/youtubers.html', data)

def youtubers_detail(request, id):
    # mixin to fetch one object
    tuber = get_object_or_404(YouTuber, pk=id)
    data ={
        'tuber':tuber
    }
    return render(request, 'youtubers/youtuber_detail.html',data)

def search(request):
    tubers = YouTuber.objects.order_by('-created_date')
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            tubers = tubers.filter(description__icontains = keyword)
    data = {
        'tubers':tubers
    }
    return render(request, 'youtubers/search.html',data)
