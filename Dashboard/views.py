from django.shortcuts import render,redirect
from Base.models import Post
from Base.models import Category
from Base.models import Announcement
from Base.models import AnnoumcementCategory

# Create your views here.
# start dashboard page views
def dashboardpageviews(request):
    china_posts=Post.objects.filter(user__china=True)
    english_posts=Post.objects.filter(user__english=True)
    myanmar_posts=Post.objects.filter(user__myanmar=True)
    context={
        'china_posts':china_posts,
        'english_posts':english_posts,
        'myanmar_posts':myanmar_posts
        }
    

    return render(request,'Dashboard/dashboard.html',context)
# start all create pages

# start post create page views
def postcreatepageviews(request):
    category=Category.objects.all()

    if request.method == 'POST':
        title=request.POST.get('name')
        category=request.POST.get('category')
        text=request.POST.get('discription')
        image=request.FILES.get('image')

        Post.objects.create(
            name=title,
            category_id=category,
            discription=text,
            images=image,
            user=request.user
            )
        if 'saveandanother' in request.POST:
            return redirect('postcreatepage')
        else:
            return redirect('allpostpage')


    context={
        'category':category
        }
    
    return render(request,'CRUD/postcreate.html',context)
# end post create page views

# start announcements create page
def announcementcreatepage(request):
    return render(request,'CRUD/announcementcreate.html')
# end announcements create page
# end all create pages

# start delete post page views
def postdeletepageviews(request,pk):
    post=Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('allpostpage')
    return render(request,'Dashboard/postall.html')
    
    
# end delete post page views

# start post  page views
def allpostpageviews(request):
    all_posts=Post.objects.filter(user__username='english')[0:7]
    context={
        'all_posts':all_posts,
        }
 
    return render(request,'Dashboard/postall.html',context)
# end post detail page views

# start statement page views
def statementpageviews(request):
    statement_posts=Post.objects.filter(user__english=True,category__name='Statement')
    context={
        'statement_posts':statement_posts
    }
    return render(request,'Dashboard/statement.html',context)
# end statement page views

# start military page views
def militarypageviews(request):
    military_posts=Post.objects.filter(user__english=True,category__name='Military')
    context={
        'military_posts':military_posts
    }
    return render(request,'Dashboard/military.html',context)
# end military page views

# start party page views
def partypageviews(request):
    party_posts=Post.objects.filter(user__english=True,category__name='Party')
    context={
        'party_posts':party_posts
    }
    return render(request,'Dashboard/party.html',context)
# end party page views

# start category create page views
def categorycreatepageviews(request):
    return render(request,'pages/category/categorycreate.html')
# end post category page views



# start category detail page views
def categoryallpageviews(request):
    return render(request,'pages/category/categoryall.html')
# end category detail page views


# post detail page views
def postdetailpageviews(request,pk):
    all_posts=Post.objects.filter(user__username='english')[0:7]
    detail_post=Post.objects.get(id=pk)
    
    context={
        'all_posts':all_posts,
        'detail_post':detail_post
     
        }
    return render(request,'CRUD/postdetail.html',context)
# post detail page views

