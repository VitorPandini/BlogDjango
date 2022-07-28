from django.shortcuts import render,HttpResponse

# Create your views here.

def post_list(request):
    return render(request,'core/post_list.html', {})