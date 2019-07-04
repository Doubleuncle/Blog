from django.shortcuts import render
from django.http import JsonResponse,HttpRequest,HttpResponse,HttpResponseBadRequest
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.db.models import Q
from .models import User,Content
# Create your views here.

def index(request):
    limit 		  = 10
    info  		  = Content.objects.exclude(isDelete=True).values().order_by('-id')
    tag   			= Content.objects.exclude(isDelete=True).values('tag').distinct()
    
    paginator   = Paginator(info, limit)
    page_range  = paginator.page_range
    
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            info = paginator.page(page)
        		# todo: 注意捕获异常
        except PageNotAnInteger:
            # 如果请求的页数不是整数, 返回第一页。
            info = paginator.page(1)
        except InvalidPage:
            # 如果请求的页数不存在, 重定向页面
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
            info = paginator.page(paginator.num_pages)
    	
    return render(request, 'index.html' ,{"info":info,"tag":tag,"page_range":page_range})
       	
def article(request):
    limit 		  = 10
    info  		  = Content.objects.exclude(isDelete=True).filter(Q(type=1)|Q(type=2)).values().order_by('-id')
    tag   			= Content.objects.exclude(isDelete=True).values('tag').distinct()
    
    paginator   = Paginator(info, limit)
    page_range  = paginator.page_range
    
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            info = paginator.page(page)
        except PageNotAnInteger:
            info = paginator.page(1)
        except InvalidPage:
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            info = paginator.page(paginator.num_pages)
    	
    return render(request, 'article.html' ,{"info":info,"tag":tag,"page_range":page_range,"article_type":"all"})
    	
def article_tecnology(request):
    limit 		  = 10
    info  		  = Content.objects.exclude(isDelete=True).filter(type=1).values().order_by('-id')
    tag   			= Content.objects.exclude(isDelete=True).values('tag').distinct()
    
    paginator   = Paginator(info, limit)
    page_range  = paginator.page_range
    
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            info = paginator.page(page)
        except PageNotAnInteger:
            info = paginator.page(1)
        except InvalidPage:
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            info = paginator.page(paginator.num_pages)
    	
    return render(request, 'article.html' ,{"info":info,"tag":tag,"page_range":page_range,"article_type":"tecnology"})
    	
def article_lifestyle(request):
    limit 		  = 10
    info  		  = Content.objects.exclude(isDelete=True).filter(type=2).values().order_by('-id')
    tag   			= Content.objects.exclude(isDelete=True).values('tag').distinct()
    
    paginator   = Paginator(info, limit)
    page_range  = paginator.page_range
    
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            info = paginator.page(page)
        except PageNotAnInteger:
            info = paginator.page(1)
        except InvalidPage:
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            info = paginator.page(paginator.num_pages)
    	
    return render(request, 'article.html' ,{"info":info,"tag":tag,"page_range":page_range,"article_type":"lifestyle"})
  	    	
def image(request):
    limit 			= 9
    info  		  = Content.objects.exclude(isDelete=True).filter(type=3).values().order_by('-id')
    tag   			= Content.objects.exclude(isDelete=True).values('tag').distinct()
    
    paginator   = Paginator(info, limit)
    page_range  = paginator.page_range
    
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            info = paginator.page(page)
        except PageNotAnInteger:
            info = paginator.page(1)
        except InvalidPage:
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            info = paginator.page(paginator.num_pages)
    return render(request, 'image.html' ,{"info":info,"tag":tag,"page_range":page_range})

    	
def voice(request):
    limit 		  = 10
    info  		  = Content.objects.exclude(isDelete=True).filter(type=4).values().order_by('-id')
    tag   			= Content.objects.exclude(isDelete=True).values('tag').distinct()
    
    paginator   = Paginator(info, limit)
    page_range  = paginator.page_range
    
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            info = paginator.page(page)
        except PageNotAnInteger:
            info = paginator.page(1)
        except InvalidPage:
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            info = paginator.page(paginator.num_pages)
    	
    return render(request, 'voice.html' ,{"info":info,"tag":tag,"page_range":page_range})

def tag(request,tags):
    tags  			= str(tags)
    limit 		  = 10
    info  		  = Content.objects.exclude(isDelete=True).filter(tag__contains=tags).values().order_by('-id')
    tag   			= Content.objects.exclude(isDelete=True).values('tag').distinct()
    
    paginator   = Paginator(info, limit)
    page_range  = paginator.page_range
    
    if request.method == "GET":
        page = request.GET.get('page')
        try:
            info = paginator.page(page)
        except PageNotAnInteger:
            info = paginator.page(1)
        except InvalidPage:
            return HttpResponse('找不到页面的内容')
        except EmptyPage:
            info = paginator.page(paginator.num_pages)
    	
    return render(request, 'tag.html' ,{"info":info,"tag":tag,"page_range":page_range,"tags":tags})
    	
def detail(request,id):
    id = int(id)
    info = Content.objects.exclude(isDelete=True).filter(id=id).values().order_by('-id')
    tag  = Content.objects.exclude(isDelete=True).values('tag').distinct()
    count = len(info)
    return render(request, 'detail.html' ,{"info":info,"tag":tag,"count":count})
    	    	
def about(request):
    return render(request, 'about.html')