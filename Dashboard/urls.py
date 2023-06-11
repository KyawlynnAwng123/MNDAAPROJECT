from django.urls import path
from .import views

urlpatterns=[
    # start dashboard urls
    path('dashboard/',views.dashboardpageviews,name="dashboardpage"),
    path('postcreate/',views.postcreatepageviews,name='postcreatepage'),
    path('announcementcreate/',views.announcementcreatepage,name='announcementcreatepage'),
    path('allpost/',views.allpostpageviews,name='allpostpage'),
    path('statement/',views.statementpageviews,name="statementpage"),
    path('military/',views.militarypageviews,name="militarypage"),
    path('party/',views.partypageviews,name="partypage"),
    path('categorycreate/',views.categorycreatepageviews,name="categorycreatepage"),
    path('allcategory/',views.categoryallpageviews,name="allcategorypage"),


    # dashboard detail urls 
    path('detail/<str:pk>/',views.postdetailpageviews,name="postdetailpage"),
    path('delete/<str:pk>/',views.postdeletepageviews,name="postdeletepage"),
 
    
]