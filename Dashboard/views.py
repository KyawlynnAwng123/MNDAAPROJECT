from django.shortcuts import render,redirect
from Base.models import Post
from Base.models import Category
from Base.models import Announcement
from Base.models import Alliance
from Base.models import AllianceCategory
from Base.models import AnnoumcementCategory
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
# start loginpage views
def loginpageviews(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username,password=password)
        except:
            messages.error(request, 'Sorry! User Does Not Exists')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('allpostpage')
    return render(request,'account/login.html')
# end loginpage views

# start logout page views
def logoutpageviews(request):
    logout(request)
    return redirect('loginpage')
# end logout page views
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
    announcement_category=AnnoumcementCategory.objects.all()
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
            return redirect('announcementcreatepage')
        else:
            return redirect('allpostpage')
    context={
        'announcement_category':announcement_category
        }
    return render(request,'CRUD/announcementcreate.html',context)
# end announcements create page

# start alliances create page
def alliancecreatepageviews(request):
    category=Category.objects.all()
    alliance_category=AllianceCategory.objects.all()
    if request.method == 'POST':
        title=request.POST.get('name')
        category=request.POST.get('category')
        alliance=request.POST.get('alliancecategory')
        text=request.POST.get('discription')
        image=request.FILES.get('image')

        Alliance.objects.create(
            name=title,
            category_id=category,
            alliancecategory_id=alliance,
            discription=text,
            images=image,
            user=request.user
            )
        if 'saveandanother' in request.POST:
            return redirect('alliancecreatepage')
        else:
            return redirect('allpostpage')
    context={
        'alliance_category':alliance_category,
        'category':category
        }
    return render(request,'CRUD/alliancescreate.html',context)
# end alliances create page

# start category create page views
def categorycreatepageviews(request):
    allcategory=Category.objects.all
    if request.method =='POST':
        categoryname=request.POST.get('category')
        Category.objects.create(
            name=categoryname

        )
        return redirect('categorycreatepage')
    context={
        'allcategory':allcategory
    }

    return render(request,'CRUD/category/categorycreate.html',context)
# end post category page views



# start category detail page views
def categoryallpageviews(request):
    return render(request,'CURD/category/categoryall.html')
# end category detail page views
# end all create pages

# start delete post page views
def postdeletepageviews(request,pk):
    post=Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('allpostpage')
    return render(request,'CRUD/postdelete.html')
# end delete post page views

# start all pages update
# start update post page views
def postupdatepageviews(request,pk):
    postupdate=Post.objects.get(id=pk)
    category=Category.objects.all()
    if request.method == 'POST':
        if request.FILES.get('image'):
            title=request.POST.get('name')
            category=request.POST.get('category')
            text=request.POST.get('discription')
            image=request.FILES.get('image')

            postupdate.name=title
            postupdate.category_id=category
            postupdate.discription=text
            postupdate.images=image

            postupdate.save()
            if 'postupdate' in request.POST:
                return redirect('allpostpage')
            
        title=request.POST.get('name')
        category=request.POST.get('category')
        text=request.POST.get('discription')
        # image=request.FILES.get('image')

        postupdate.name=title
        postupdate.category_id=category
        postupdate.discription=text
        #  postupdate.images=image
        postupdate.save()
        return redirect('allpostpage')
    return render(request,'CRUD/postupdate.html',{'postupdate':postupdate,'category':category})

        
        
# end update post page views

# start update statement page views
def statementupdatepageviews(request,pk):
    postupdate=Post.objects.get(id=pk)
    category=Category.objects.all()
    if request.method == 'POST':
        if request.FILES.get('image'):
            title=request.POST.get('name')
            category=request.POST.get('category')
            text=request.POST.get('discription')
            image=request.FILES.get('image')

            postupdate.name=title
            postupdate.category_id=category
            postupdate.discription=text
            postupdate.images=image

            postupdate.save()
            if 'postupdate' in request.POST:
                return redirect('statementpage')
            
        title=request.POST.get('name')
        category=request.POST.get('category')
        text=request.POST.get('discription')
        # image=request.FILES.get('image')

        postupdate.name=title
        postupdate.category_id=category
        postupdate.discription=text
        #  postupdate.images=image
        postupdate.save()
        return redirect('statementpage')
    return render(request,'CRUD/statementupdate.html',{'postupdate':postupdate,'category':category})
# end update statement post page views


# start post  page views
def allpostpageviews(request):
    
    all_posts=Post.objects.all()[0:20]
    context={
        'all_posts':all_posts,
        }
 
    return render(request,'Dashboard/postall.html',context)
# end post detail page views

# start statement page views
def statementpageviews(request):
    
    statement_posts=Post.objects.filter(category__name='Statement')
    context={
        'statement_posts':statement_posts
    }
    return render(request,'Dashboard/statement.html',context)
# end statement page views

# start military page views
def militarypageviews(request):
    military_posts=Post.objects.filter(category__name='Military')
    context={
        'military_posts':military_posts
    }
    return render(request,'Dashboard/military.html',context)
# end military page views

# start party page views
def partypageviews(request):
    party_posts=Post.objects.filter(category__name='Party')
    context={
        'party_posts':party_posts
    }
    return render(request,'Dashboard/party.html',context)
# end party page views




# post detail page views
def postdetailpageviews(request,pk):
    all_posts=Post.objects.all()[0:7]
    detail_post=Post.objects.get(id=pk)
    
    context={
        'all_posts':all_posts,
        'detail_post':detail_post
     
        }
    return render(request,'CRUD/postdetail.html',context)
# post detail page views

