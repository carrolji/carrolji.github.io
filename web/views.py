from django.shortcuts import render
from .models import BucketList, ProjectList

def index(request):
    return render(request, 'index.html', {})

def bucket_list(request):
    bucket_checked = BucketList.objects.filter(complete=True).order_by('order')
    to_do = BucketList.objects.filter(complete=False).order_by('order')
    context = {
        'bucket_checked': bucket_checked,
        'bucket_unchecked' : to_do,
    }
    return render(request, 'bucketlist/bucket_list.html', context)