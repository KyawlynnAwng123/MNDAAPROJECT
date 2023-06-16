from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from Base.models import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


# start indexpage views
def myanmarindexpageviews(request):
    #statement component 
    last_post_statement=Post.objects.filter(category__name='Statement',user__username='myanmar')[:1]
    last_two_post_statement=Post.objects.filter(category__name='Statement',user__username='myanmar')[1:]
    #end
    #military component
    last_post_military=Post.objects.filter(category__name='Military',user__username='myanmar')[:1]
    last_post_three_military=Post.objects.filter(category__name='Military',user__username='myanmar')[1:]
    # end

    # party conponent
    last_post_party=Post.objects.filter(category__name='Party',user__username='myanmar')[:1]
    last_two_post_party=Post.objects.filter(category__name='Party',user__username='myanmar')[1:]


    context={
        'last_post_statement':last_post_statement,
        'last_two_post_statement':last_two_post_statement,
        'last_post_military':last_post_military,
        'last_post_three_military':last_post_three_military,
        'last_post_party':last_post_party,
        'last_two_post_party':last_two_post_party
        }

    
    return render(request,'page/index.html',context)
# end indexpage views


# start newspage views
def myan_newspageviews(request):
    latest_post=Post.objects.filter(user__username='myanmar')[:1]
    latest_two_posts=Post.objects.filter(user__username='myanmar')[2:4]
    latest_three_posts=Post.objects.filter(user__username='myanmar')[4:7]
    all_posts=Post.objects.filter(user__username='myanmar')[1:7]
    context={
        'latest_post':latest_post,
        'latest_two_posts':latest_two_posts,
        'latest_three_posts':latest_three_posts,
        'all_posts':all_posts
        }
    return render(request,'page/myan_news/myan_news.html',context)
# end newspage views


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
            return redirect('dashboardpage')
       
    return render(request,'account/login.html')
# end loginpage views

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
    

    return render(request,'account/dashboard.html',context)
# end dashboard page views


# start logout page views
def logoutpageviews(request):
    logout(request)
    return redirect('loginpage')
# end logout page views


# start military in nation
def myan_militarypageviews(request):
    page=request.GET.get('page')
    latest_posts_military_nation=Post.objects.filter(category__name='Military',user__username='myanmar')[:1]
    military_posts_nation=Post.objects.filter(category__name='Military',user__username='myanmar')[1:]

    paginator=Paginator(military_posts_nation,4)

    try:
        military_posts_nation=paginator.page(page)

    except PageNotAnInteger:
        military_posts_nation=paginator.page(1)

    except EmptyPage:
        military_posts_nation=military_posts_nation(1)

    

    context={
        'latest_posts_military_nation':latest_posts_military_nation,
        'military_posts_nation':military_posts_nation,
        'paginator':paginator
        }
    return render(request,'page/myan_nation/myan_nation_military.html',context)
# end military in nation

# start party in nation
def myan_partypageviews(request):
    page=request.GET.get('page')
    myan_latest_post_nation_party=Post.objects.filter(category__name='Party',user__username='myanmar')[:1]
    party_posts_nation=Post.objects.filter(category__name='Party',user__username='myanmar')[1:]

    paginator=Paginator(party_posts_nation,4)

    try:
        party_posts_nation=paginator.page(page)

    except PageNotAnInteger:
        party_posts_nation=paginator.page(1)

    except EmptyPage:
        party_posts_nation=paginator(1)
    context={
        'party_posts_nation':party_posts_nation,
        'myan_latest_post_nation_party':myan_latest_post_nation_party,
        'paginator':paginator


        }
    return render(request,'page/myan_nation/myan_nation_party.html',context)
# end party in nation

# statement in announcements
def myan_statement_announcements(request):
    statement_announcements=Post.objects.filter(category__name='Statement',user__username='myanmar')[:1]
    statements_announcements=Post.objects.filter(category__name='Statement',user__username='myanmar')[1:]

    context={
        'statement_announcements':statement_announcements,
        'statements_announcements':statements_announcements
        }
    return render(request,'page/myan_announcement/myan_statement/myan_statement.html',context)
# statement in announcements


# speech in announcements
def speech_announcements(request):
    return render(request,'pages/announcements/speech/speech.html')
# speech in announcements



# interview in announcements
def interview_announcements(request):
    return render(request,'pages/announcements/interview/interview.html')
# interview in announcements


# alliences pageviews
# fpncc in alliences
def myan_fpnccp_allience(request):
    latest_post=Alliance.objects.filter(alliancecategory__name='FPNCC',user__username='myanmar')[:1]
    context={
        'latest_post':latest_post
    }
    return render(request,'page/myan_alliences/myan_fpncc/myan_fpncc.html',context)
# fpncc in alliences


# northern-allienc page views
def myan_northern_allience(request):
    n_alliance=Alliance.objects.filter(alliancecategory__name='Northern Alliance',user__username='myanmar')[:1]
    context={
        'n_alliance':n_alliance
    }
    return render(request,'page/myan_alliences/myan_northernallience/myan_northernallience.html',context)
# northern-allienc page views



# start all detail 

# start statement detail
def myan_statementdetailpage(request,pk):
    myan_statement_detail_post=Post.objects.get(id=pk)
    myan_related_posts_statementview=Post.objects.filter(category=myan_statement_detail_post.category,user__username='myanmar')
    
    
    context={
        'myan_statement_detail_post':myan_statement_detail_post,
        'myan_related_posts_statementview':myan_related_posts_statementview
        }
    return render(request,'lifeside/myan_statement/myan_statementview.html',context)
# end statement detail

# start military detail
def myan_militarydetailpage(request,pk):
    military_detail_post=Post.objects.get(id=pk)
    myan_military_related_posts=Post.objects.filter(category=military_detail_post.category,user__username='myanmar')


    context={
        'military_detail_post':military_detail_post,
        'myan_military_related_posts':myan_military_related_posts
        }
    return render(request,'lifeside/myan_military/myan_militarydetail.html',context)
# end military detail

# start party detail pageviews
def myan_partydetailpage(request,pk):
    myan_party_detail_post=Post.objects.get(id=pk)
    myan_party_related_posts=Post.objects.filter(category=myan_party_detail_post.category,user__username='myanmar')

    context={
        'myan_party_detail_post':myan_party_detail_post,
        'myan_party_related_posts':myan_party_related_posts
        }
    return render(request,'lifeside/myan_party/myan_partydetail.html',context)
# end party detail pageviews





