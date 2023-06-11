from django.urls import path
from .import views

url='myanmar'

urlpatterns = [
    path('myan/',views.myanmarindexpageviews,name="myanmarpage"),
    path('myan_news/',views.myan_newspageviews,name="myan_news_page"),

    # start mya_nation urls
    path('myan_nation_military/',views.myan_militarypageviews,name="myan_nation_militarypage"),
    path('myan_nation_party/',views.myan_partypageviews,name="myan_nation_partypage"),


    # start announcemnts urls
    path('myan_announcement_statement/',views.myan_statement_announcements,name="myan_announ_statement_page"),


    # start alliances urls 
    path('myan_fpncc/',views.myan_fpnccp_allience,name="myan_fpncc_page"),

    # start detail urls
    path('myan_statement/<str:pk>/',views.myan_statementdetailpage,name="myan_statement_detail_page"),
    path('myan_military/<str:pk>/',views.myan_militarydetailpage,name="myan_military_detail_page"),
    path('myan_party/<str:pk>/',views.myan_partydetailpage,name="myan_party_detail_page"),

    
]
