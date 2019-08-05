from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpRequest,HttpResponse,HttpResponseBadRequest
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q,Max
from .models import User,Content
from .forms import UserForm
import os
# Create your views here.

#管理
def login(request):
    if request.session.get('is_login', None):
        return render(request,'admin.html')
        	      
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if user.password == password:
                    request.session['is_login']  = True
                    request.session['user_id']   = user.id
                    request.session['user_name'] = user.name
                    return redirect('/admin/')
                else:
                    message = "密码不正确!"
            except:
                message = '用户不存在!'
        return render(request, 'login.html', locals())
 
    login_form = UserForm()
    return render(request, 'login.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/")
    request.session.flush()
    return redirect("/")
	
def admin(request):
    return render(request,'admin.html')

@csrf_protect
def upload(request):
    if request.method == "POST":
        try:
            upload_type = request.POST.get('upload_type') 
            if upload_type == '1' or upload_type == '2':           	  
                article_title 	= request.POST.get('article_title')
                article_content =request.POST.get('article_content')
                article_tag 		= request.POST.get('article_tag')
                Content.objects.create(type=upload_type,title=article_title,content=article_content,tag=article_tag)
                return JsonResponse({"code":"200"})
            elif upload_type == '3':
                image_title 	= request.POST.get('image_title')
                image_content = request.POST.get('image_content')
                image_tag 		= request.POST.get('image_tag')
                file_data     = request.FILES.get('file')
                Content.objects.create(type=upload_type,title=image_title,content=image_content,tag=image_tag)
                file_name 		= str(Content.objects.all().aggregate(Max('id'))['id__max']) + '.png'
                BASE_DIR 		  = os.path.dirname(os.path.abspath(__file__))
                path				  = os.path.join(os.path.join(BASE_DIR, 'static'),'image')
                with open(os.path.join(path, file_name),'wb+') as f:
                    for chunk in file_data.chunks():
                        f.write(chunk)
                return JsonResponse({"code":"200"})
            elif upload_type == '4':
                voice_title 	= request.POST.get('voice_title')
                voice_content = request.POST.get('voice_content')
                voice_tag 		= request.POST.get('voice_tag')
                file_data     = request.FILES.get('file')
                Content.objects.create(type=upload_type,title=voice_title,content=voice_content,tag=voice_tag)
                file_name 		= str(Content.objects.all().aggregate(Max('id'))['id__max']) + '.mp3'
                BASE_DIR 		  = os.path.dirname(os.path.abspath(__file__))
                path				  = os.path.join(os.path.join(BASE_DIR, 'static'),'voice')
                with open(os.path.join(path, file_name),'wb+') as f:
                    for chunk in file_data.chunks():
                        f.write(chunk)
                return JsonResponse({"code":"200"})
            elif request.FILES.get('file'):
                return JsonResponse({"file":"file"})
            return JsonResponse({"b":request.POST.get('aaa')})
        except Exception as e:
        	  return JsonResponse({"code":str(e)})
        
    return JsonResponse({"a":request.method})

#展现   
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
    	
    return render(request, 'index.html' ,locals())
	            	
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
    return render(request, 'image.html' ,locals())

    	
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
    	
    return render(request, 'voice.html' ,locals())

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
    	
    return render(request, 'tag.html' ,locals())
    	
def detail(request,id):
    id = int(id)
    info = Content.objects.exclude(isDelete=True).filter(id=id).values().order_by('-id')
    tag  = Content.objects.exclude(isDelete=True).values('tag').distinct()
    return render(request, 'detail.html' ,locals())
    	    	
def about(request):
    return render(request, 'about.html')
    
#错误处理
def page_not_found(request,exception):
    return render(request, 'error.html',status=404)
 
def page_error(request):
    return render(request, 'error.html',status=500)
